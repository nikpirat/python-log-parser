# config.py

# Path to the input log file (can be overridden via CLI or env vars)
LOG_FILE_PATH = "logs/sample.log"

# Path to the output CSV file
OUTPUT_FILE_PATH = "output/errors.csv"

# HTTP status codes to filter for
FILTER_STATUS_CODES = {"500"}  # You can add "404", etc.

# Regular expression pattern for Apache-style logs
LOG_PATTERN = (
    r'(?P<ip>\S+) - - '
    r'\[(?P<datetime>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<url>\S+) (?P<protocol>[^"]+)" '
    r'(?P<status>\d{3}) '
    r'(?P<size>\d+)'
)

# CSV column order
CSV_FIELDS = ["ip", "datetime", "method", "url", "protocol", "status", "size"]