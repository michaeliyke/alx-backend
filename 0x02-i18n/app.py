#!/usr/bin/env python3
"""Internationlization (i18n) and localization (l10n) with Flask"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime, _  # type: ignore
from typing import List, Union, Optional
import logging
import pytz
from datetime import datetime


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
    # Locale from URL parameters

    locale = request.args.get("locale", None)
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    # Locale from user settings
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user.get("locale")

    # Locale from request header
    header_locale = request.headers.get("Accept-Language")
    if header_locale:
        header_locales = header_locale.replace(" ", "").split(",")
        for locale in header_locales:
            if locale in app.config["LANGUAGES"]:
                return locale

    # Default locale
    return app.config["BABEL_DEFAULT_LOCALE"]


@babel.timezoneselector
def get_timezone() -> Optional[str]:
    """Get time zone from request"""
    # Time zone from URL parameters
    timezone = request.args.get("timezone", None)
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # Time zone from user settings
    if g.user and g.user.get("timezone"):
        try:
            pytz.timezone(g.user.get("timezone"))
            return g.user.get("timezone")
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # Default time zone
    return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET /
    Return: 1-index.html
    """
    # use the preffered timezone
    timezone = get_timezone()
    # Get the current date and time in the determined timezone
    my_date = datetime.now(pytz.timezone(timezone))
    # my_date = datetime.now()

    print("my_date: ", my_date)
    print("timezone: ", timezone)

    # Format the date as a string
    formatted = format_datetime(my_date, format="medium")

    # Pass the formatted datetime to the template
    return render_template(
        "index.html",
        user=g.get("user", None),
        my_date=formatted,
    )


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
    # command to run: python3 -m 0-app
