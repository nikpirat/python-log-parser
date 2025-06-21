import csv

from parser.filters import filter_errors
from parser.parser import parse_log_lines
from parser.writer import write_to_csv
from tests.test_reader import sample_logs


def test_write_to_csv(tmp_path):
    parsed = list(parse_log_lines(sample_logs))
    errors = list(filter_errors(parsed, status_code="500"))

    output_path = tmp_path / "errors.csv"
    write_to_csv(errors, str(output_path))

    with open(output_path, newline='') as f:
        reader = list(csv.DictReader(f))
        assert len(reader) == 1
        assert reader[0]["status"] == "500"
        assert reader[0]["ip"] == "10.0.0.2"