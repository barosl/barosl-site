from . import app
import flask
import datetime

@app.route('/')
def index():
    uptime = str(datetime.timedelta(seconds=int(float(open('/proc/uptime').read().split()[0]))))
    return flask.render_template('index.html', uptime=uptime)
