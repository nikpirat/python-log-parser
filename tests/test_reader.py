# Sample Apache log lines
from parser.reader import read_log_lines

sample_logs = [
    '127.0.0.1 - - [21/Jun/2025:10:15:42 +0000] "GET /index.html HTTP/1.1" 200 1043',
    '10.0.0.2 - - [21/Jun/2025:10:16:15 +0000] "GET /dashboard HTTP/1.1" 500 2341',
]
def test_read_log_lines(tmp_path):
    log_file = tmp_path / "test.log"
    log_file.write_text("\n".join(sample_logs))

    lines = list(read_log_lines(str(log_file)))
    assert len(lines) == 2
    assert lines[0].startswith("127.0.0.1")