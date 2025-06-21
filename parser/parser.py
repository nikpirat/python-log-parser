import re


def parse_log_lines(lines):
    log_pattern = re.compile(
        r'(?P<ip>\S+) - - \[(?P<datetime>[^]]+)] '
        r'"(?P<method>\S+) (?P<url>\S+) (?P<protocol>[^"]+)" '
        r'(?P<status>\d{3}) (?P<size>\d+)'
    )

    for line in lines:
        match = log_pattern.match(line)
        if match:
            yield match.groupdict()
        else:
            continue  # or log malformed lines