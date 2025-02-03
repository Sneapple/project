import logging
import requests

# Set up logging
logging.basicConfig(level=logging.INFO)

def scan_open_redirect(url):
    """
    Scans a URL for potential open redirect vulnerabilities.
    
    Args:
        url (str): The URL to be scanned.
    
    Returns:
        bool: True if an open redirect vulnerability is detected, False otherwise.
    """
    logging.info(f"Scanning URL: {url} for potential open redirect vulnerabilities.")
    
    # Common open redirect payloads that could be used to trigger the vulnerability
    open_redirect_payloads = [
        "http://example.com",  # A harmless redirect to demonstrate the concept
        "http://evil.com",  # A malicious URL for testing open redirect
        "https://malicious.com",  # Another potential malicious redirect
    ]
    
    for payload in open_redirect_payloads:
        redirect_url = f"{url}?next={payload}"  # Assuming the URL has a `next` parameter for redirection
        
        try:
            response = requests.get(redirect_url, allow_redirects=False)  # Don't follow redirects
            
            if response.status_code == 302:  # 302 is typically a redirect response
                logging.warning(f"Potential Open Redirect vulnerability detected at {redirect_url}")
                return True  # If we detect a redirect, this is an indication of a potential open redirect vulnerability
        except requests.exceptions.RequestException as e:
            logging.error(f"Error scanning {url}: {e}")
            return False
    
    logging.info(f"No open redirect vulnerabilities detected at {url}")
    return False
