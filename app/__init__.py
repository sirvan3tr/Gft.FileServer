from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine(app)
UPLOAD_FOLDER = 'app/uploads/'

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'project1',
    'host': '192.168.1.35',
    'port': 12345
}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

from app import routesmongo