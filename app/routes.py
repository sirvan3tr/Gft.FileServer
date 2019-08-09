import os
from app import app
from flask import render_template, session, redirect, url_for, escape, request, send_from_directory
from werkzeug.utils import secure_filename
import json

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html')


@app.route('/plot', methods=['GET', 'POST'])
def plot():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(filename)
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('plot.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads/',
                               filename)


@app.route('/geocode')
def geocode():
    return "hello"


@app.route('/getfile/<file>', methods=['POST'])
def getfile(file):
    return send_from_directory('uploads/',
                               filename)


@app.route('/uploadfile', methods=['POST'])
def uploadfile():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(filename)
        return redirect(url_for('uploaded_file', filename=filename))
    return render_template('plot.html')


@app.route('/master', methods=['POST'])
def master():
    req_data = request.get_json()
    return json.dumps(req_data)
