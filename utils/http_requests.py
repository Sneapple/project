# utils/http_requests.py

import requests
import logging

def send_request(url: str):
    """
    Send a GET request to the given URL and return the response.
    
    Args:
        url (str): The URL to send the request to.
    
    Returns:
        response: The response object from the request or None if there was an error.
    """
    try:
        logging.info(f"Sending request to {url}")
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        logging.info(f"Received response with status code: {response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"Error while sending request to {url}: {e}")
        return None
