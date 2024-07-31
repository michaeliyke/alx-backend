#!/usr/bin/env python3
"""
Internationlization (i18n) and localization (l10n) with Flask
"""

# import flask
# from flask_babel import Babel # type: ignore

# app = flask.Flask(__name__)
# babel = Babel(app)


class Config:
    """Babel configuration class for app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# app.config.from_object(Config)


# @app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """Returns the index page for the app"""
    # return flask.render_template("1-index.html")


if __name__ == "__main__":
    pass
    # app.run(host="localhost", port=5000, debug=True)
    # command to run: python3 -m 0-app
