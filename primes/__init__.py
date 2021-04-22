"""App initializer."""

import flask

app = flask.Flask(__name__)


# Overlay settings read from a Python file whose path is set in the environment
# variable INSTA485_SETTINGS. Setting this environment variable is optional.
# Docs: http://flask.pocoo.org/docs/latest/config/
#
# EXAMPLE:
# $ export INSTA485_SETTINGS=secret_key_config.py
# app.config.from_envvar('SEARCH_SETTINGS', silent=True)

import primes.views
