#!/usr/bin/python3
""" Docstrings"""

from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route("/admin")

@app.rout("/user/<name>")
def hello_user(name):
    if name == "admin":
                return redirect(url_for("hello_admin"))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

