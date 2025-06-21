from parser.filters import filter_errors
from parser.parser import parse_log_lines
from tests.test_reader import sample_logs


def test_filter_errors():
    parsed = list(parse_log_lines(sample_logs))
    errors = list(filter_errors(parsed, status_code="500"))

    assert len(errors) == 1
    assert errors[0]["status"] == "500"
    assert errors[0]["ip"] == "10.0.0.2"