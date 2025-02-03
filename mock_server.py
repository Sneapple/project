# mock_server.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if "' OR 1=1 --" in password:
        return "SQL error", 500  # Simulate a SQL injection error
    return "Login successful", 200

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
