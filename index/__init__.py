SECRET_KEY = b'development key'

import flask

app = flask.Flask(__name__)

app.config.from_object(__name__)
app.config.from_envvar('APP_CFG', silent=True)

from . import views
