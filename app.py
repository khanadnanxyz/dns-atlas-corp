from flask import Flask
from config import config
from api import v1
from api.v1.routes import mod, limiter
import flask_monitoringdashboard as dashboard

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

limiter.init_app(app)

dashboard.bind(app)
dashboard.config.init_from(file='./config/dashboard_config.cfg')


@app.route('/')
def hello_world():
    return 'Hello, Space!'


app.register_blueprint(v1.routes.mod, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
