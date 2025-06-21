from config import LOG_FILE_PATH
from parser.reader import read_log_lines
from parser.parser import parse_log_lines
from parser.filters import filter_errors
from parser.writer import write_to_csv

def main():
    lines = read_log_lines(LOG_FILE_PATH)
    parsed = parse_log_lines(lines)
    errors = filter_errors(parsed, status_code='500')
    write_to_csv(errors, "output/errors.csv")

if __name__ == "__main__":
    main()