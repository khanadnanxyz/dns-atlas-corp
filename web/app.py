from flask import Flask, jsonify

from web import api
from web.api.v1.routes import limiter
from web.config import config

import flask_monitoringdashboard as dashboard

app = Flask(__name__)
app.config.from_object(config.ProductionConfig)

limiter.init_app(app)

dashboard.bind(app)
dashboard.config.init_from(file='config/dashboard_config.cfg')


@app.route('/')
def hello_world():
    data = {
        'status': 'OK',
        'message': 'hello, space!'
    }
    return jsonify(data), 200


app.register_blueprint(api.v1.routes.mod, url_prefix='/api/v1')
