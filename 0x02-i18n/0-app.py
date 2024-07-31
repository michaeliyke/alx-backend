#!/usr/bin/env python3
"""Internationlization (i18n) and localization (l10n) with Flask"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _  # type: ignore
from typing import List, Union, Optional

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Babel configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Optional[str]:
    """Get locale from request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET /
    Return: 1-index.html
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
    # command to run: python3 -m 0-app
