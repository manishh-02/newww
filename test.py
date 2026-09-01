from flask import Flask, request
import sqlite3
import json

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    conn = sqlite3.connect("users.db")

    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    result = conn.execute(query).fetchone()

    return str(result)


@app.route("/load")
def load():
    data = request.args.get("data")

    # Safe deserialization using json
    obj = json.loads(data)

    return str(obj)


@app.route("/run")
def run():
    code = request.args.get("code")

    # Arbitrary code execution
    result = eval(code)

    return str(result)


if __name__ == "__main__":
    app.run(debug=True)
