from flask import Flask

UPLOAD_FOLDER = 'app/uploads/'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

from app import routes