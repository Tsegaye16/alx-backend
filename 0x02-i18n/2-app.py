#!/usr/bin/env python3
"""
Setup a basic flask application
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    creating Config class that has a LANGUAGES
    class attribute equal to ["en", "fr"].
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


"""
instantiate the Babel object in your app
"""
app = Flask(__name__)
app.config.from_object(Config)

"""
Wrapping the application with Babel
"""
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Gets locale from request object
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Returning a basic html page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
