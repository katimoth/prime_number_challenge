"""App initializer."""

import flask

app = flask.Flask(__name__)

import primes.views
