#!/usr/bin/env python3
"""Internationlization (i18n) and localization (l10n) with Flask"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, refresh, _  # type: ignore
from typing import List, Union, Optional
import logging


class Config:
    """Babel configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    return users.get(user_id)


@app.before_request
def before_request():
    user_id = request.args.get("login_as")
    g.user = get_user(int(user_id)) if user_id else None


@babel.localeselector
def get_locale() -> Optional[str]:
    """Get locale from request"""
    locale = request.args.get("locale", None)

    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET /
    Return: 1-index.html
    """
    return render_template("5-index.html", user=g.get("user", None))


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
    # command to run: python3 -m 0-app
