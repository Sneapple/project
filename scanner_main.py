import logging
from scanner.sql_injection import scan_sql_injection

def main():
    logging.basicConfig(level=logging.DEBUG)

    url = input("Enter the URL to scan for SQL injection: ")
    result = scan_sql_injection(url)
    
    if result:
        print("SQL Injection vulnerability detected!")
    else:
        print("No SQL Injection vulnerability detected.")

if __name__ == "__main__":
    main()
