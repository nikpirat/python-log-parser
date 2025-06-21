def filter_errors(parsed_logs, status_code='500'):
    for log in parsed_logs:
        if log['status'] == status_code:
            yield log