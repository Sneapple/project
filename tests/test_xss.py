import unittest
from scanner.xss import scan_xss

class TestXSSDetection(unittest.TestCase):

    def test_xss_detected(self):
        # URL that should trigger an XSS vulnerability (contains common payload)
        url_with_xss = "http://example.com?search=<script>alert('XSS')</script>"
        result = scan_xss(url_with_xss)
        print(f"Test result (XSS detected): {result}")  # This will print the result
        self.assertTrue(result)  # Expect True when XSS is detected

    def test_xss_not_detected(self):
        # URL that should NOT trigger an XSS vulnerability (does not contain any known payloads)
        url_without_xss = "http://example.com?search=hello"
        result = scan_xss(url_without_xss)
        print(f"Test result (no XSS): {result}")  # This will print the result
        self.assertFalse(result)  # Expect False when no XSS is detected

if __name__ == '__main__':
    unittest.main()
