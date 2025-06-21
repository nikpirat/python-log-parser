from parser.reader import read_log_lines
from parser.parser import parse_log_lines
from parser.filters import filter_errors
from parser.writer import write_to_csv

def test_pipeline_end_to_end(tmp_path):
    sample_log = tmp_path / "test.log"
    sample_log.write_text('10.0.0.1 - - [21/Jun/2025:10:00:00 +0000] "GET /err HTTP/1.1" 500 123\n')

    lines = read_log_lines(str(sample_log))
    parsed = parse_log_lines(lines)
    errors = filter_errors(parsed, status_code="500")

    output_csv = tmp_path / "output.csv"
    write_to_csv(errors, str(output_csv))

    assert output_csv.exists()
    assert output_csv.read_text().count("500") == 1