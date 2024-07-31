#!/usr/bin/env python3
"""Internationlization (i18n) and localization (l10n) with Flask"""

from flask import Flask, render_template

app = Flask(__name__)



@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """Returns the index page for the app"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
    # command to run: python3 -m 0-app
