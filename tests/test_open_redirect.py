# tests/test_open_redirect.py

import unittest
from scanner.open_redirect import scan_open_redirect

class TestOpenRedirect(unittest.TestCase):

    def test_open_redirect_detected(self):
        # URL that should trigger an open redirect
        result = scan_open_redirect("http://httpbin.org/redirect/1")
        print(f"Test result (open redirect): {result}")  # This will print the result
        self.assertTrue(result)  # Expect True when the open redirect is detected

if __name__ == '__main__':
    unittest.main()
# tests/test_open_redirect.py

import unittest
from scanner.open_redirect import scan_open_redirect

class TestOpenRedirect(unittest.TestCase):

    def test_open_redirect_not_detected(self):
        # URL that should NOT trigger an open redirect
        result = scan_open_redirect("http://example.com")
        print(f"Test result (no open redirect): {result}")  # This will print the result
        self.assertFalse(result)  # Expect False when no open redirect is detected

if __name__ == '__main__':
    unittest.main()

