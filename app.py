from flask import Flask
from MangroveHealth import MangroveHealth
from datetime import datetime
from flask import flash, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    mh = MangroveHealth()
    currenttime = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    return "<p>"+mh.test()+"</p><p>"+currenttime+"</p>"

def allowed_file(filename):
    extensions = ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG']
    filename, fileextension = os.path.splitext(filename)
    return fileextension in extensions

@app.route('/process_', methods=['POST'])
def process_instance_segmentation():
    if 'file' not in request.files:
        return "No file given", 400
    file = request.files['file']
    if file.filename == '':
        return "No file given", 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join("cache/", filename))
        return {}

# serve cache ..
@app.route('/cache/<path:path>')
def send_cache(path):
    if os.path.isfile(os.path.join("cache",path)):
        return send_from_directory('cache/', path)
    else : 
        return "No file", 400