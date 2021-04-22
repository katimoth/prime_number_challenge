"""Prime number challenge views."""

"""App routes."""

import json
import flask
import primes


@primes.app.route('/', methods=["GET"])
def get_index():
    """Render index."""
    result = flask.request.args.get("result")
    if not result:
        return flask.render_template("index.html")
    context = {
        "result": result,
        "isResponse": True
    }
    return flask.render_template("index.html", **context)

@primes.app.route('/', methods=["POST"])
def evaluate():
    """Evaluate input."""
    text = flask.request.form["text"]
    try:
        text = int(text)
    except ValueError:
        text = f"\'{text}\' is not a valid input. Please try again."
        return flask.redirect(flask.url_for("get_index", result=text))
    num = text
    if (num < 2):
        return flask.redirect(flask.url_for("get_index", result="No"))
    for i in range(2,(num // 2) + 1):
        if num % i == 0:
            return flask.redirect(flask.url_for("get_index", result="No"))
    return flask.redirect(flask.url_for("get_index", result="Yes"))