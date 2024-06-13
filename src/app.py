from flask import Flask
from dotenv import load_dotenv
import os

from config.mongodb import mongo
from routes.to_do import to_do
from routes.documentos import documentos

load_dotenv()
app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(app)


@app.route('/')
def index():
    return 'Hello World'

app.register_blueprint(to_do, url_prefix='/to_do')
app.register_blueprint(documentos, url_prefix='/documentos')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')