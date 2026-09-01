from flask import Flask, request
import sqlite3
import pickle

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

    # Insecure deserialization
    obj = pickle.loads(data.encode())

    return str(obj)


@app.route("/run")
def run():
    code = request.args.get("code")

    # Arbitrary code execution
    result = eval(code)

    return str(result)


if __name__ == "__main__":
    app.run(debug=True)
