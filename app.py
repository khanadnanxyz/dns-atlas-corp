from flask import Flask, jsonify
from config import config
from api import v1
from api.v1.routes import mod, limiter
import flask_monitoringdashboard as dashboard

app = Flask(__name__)
app.config.from_object(config.ProductionConfig)

limiter.init_app(app)

dashboard.bind(app)
dashboard.config.init_from(file='./config/dashboard_config.cfg')


@app.route('/')
def hello_world():
    data = {
        'status': 'OK',
        'message': 'hello, space!'
    }
    return jsonify(data), 200


app.register_blueprint(v1.routes.mod, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
