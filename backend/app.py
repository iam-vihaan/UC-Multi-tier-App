from flask import Flask
from routes import api
from config import db

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
