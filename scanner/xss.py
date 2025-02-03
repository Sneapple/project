import re
import logging
from utils.http_requests import send_request

# Set up logging
logging.basicConfig(level=logging.INFO)

def scan_xss(url: str) -> bool:
    """
    Scan for potential XSS vulnerability in a given URL by checking for common XSS attack patterns.
    
    Args:
        url (str): The URL to be scanned.
    
    Returns:
        bool: True if an XSS vulnerability is detected, False otherwise.
    """
    logging.info(f"Scanning URL: {url} for potential XSS vulnerabilities.")

    # Simple payloads that can trigger XSS vulnerabilities
    xss_payloads = [
        "<script>alert('XSS')</script>",
        "javascript:alert('XSS')",
        "onerror=alert('XSS')",
        "<img src='x' onerror='alert(1)'>"
    ]
    
    # Send a request to the URL and get the response
    try:
        response = send_request(url)
        if not response:
            logging.error(f"Failed to get a valid response from {url}")
            return False
    except Exception as e:
        logging.error(f"Error in sending request to {url}: {e}")
        return False

    # Check for XSS payloads in the URL or response body
    for payload in xss_payloads:
        if payload in url or payload in response.text:
            logging.warning(f"Potential XSS vulnerability detected at {url}")
            return True
    
    logging.info(f"No XSS vulnerabilities detected at {url}")
    return False

