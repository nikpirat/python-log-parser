from parser.parser import parse_log_lines


def test_parser_extracts_fields_correctly():
    logs = ['127.0.0.1 - - [21/Jun/2025:10:00:00 +0000] "GET /home HTTP/1.1" 200 1234']
    parsed = list(parse_log_lines(logs))
    assert parsed[0]["ip"] == "127.0.0.1"
    assert parsed[0]["method"] == "GET"
    assert parsed[0]["status"] == "200"
