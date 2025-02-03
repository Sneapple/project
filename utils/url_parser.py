# utils/url_parser.py

from urllib.parse import urlparse, parse_qs

def parse_url_for_input_fields(url):
    """
    Parses the given URL and returns a dictionary of query parameters.
    Handles cases where parameters contain '=' in the value (e.g., SQLi payloads).
    """
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)  # parse_qs handles multiple '=' in values
    return {key: value[0] for key, value in query_params.items()}  # Take the first value from the list
