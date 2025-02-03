# tests/test_sql_injection.py
import unittest
from scanner.sql_injection import scan_sql_injection

class TestSQLInjection(unittest.TestCase):

    def test_sql_injection_detected(self):
        # Simulate a URL that triggers SQL injection
        url_with_sqli = "http://localhost:5000/login?username=admin&password=' OR 1=1 --"
        result = scan_sql_injection(url_with_sqli)
        print(f"Test result (SQLi detected): {result}")  # Should print True if SQLi is detected
        self.assertTrue(result)  # Expect True when SQL injection is detected

    def test_sql_injection_not_detected(self):
        # Simulate a URL that does NOT trigger SQL injection
        url_safe = "http://localhost:5000/login?username=admin&password=admin123"
        result = scan_sql_injection(url_safe)
        print(f"Test result (no SQLi): {result}")  # Should print False if no SQLi
        self.assertFalse(result)  # Expect False when no SQL injection is detected

    def test_sql_injection_empty(self):
        # Test with an empty URL (edge case)
        url_empty = ""
        result = scan_sql_injection(url_empty)
        self.assertFalse(result)  # Expect False for empty URL

if __name__ == '__main__':
    unittest.main()
