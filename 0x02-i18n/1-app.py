#!/usr/bin/env python3
"""Internationlization (i18n) and localization (l10n) with Flask"""

from flask import Flask, render_template
from flask_babel import Babel # type: ignore

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Babel configuration class for app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

