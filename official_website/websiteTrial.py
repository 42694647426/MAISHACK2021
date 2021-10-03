from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
import sys
import numpy as np
from PIL import Image

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(BASE_DIR)
from ML_model import predict

 
app = Flask(__name__)
# app.config.from_object("config.DevelopmentConfig")
UPLOAD_FOLDER = 'static/uploads/'
# print(app.config)
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

FLOWER_TYPE = [
    'alfalfa' ,
    'allium'      ,
    'borage' ,
    'calendula' ,
    'chicory'  ,
    'chive_blossom',
    'common_mallow',
    'coneflower'  ,
    'cowslip'     ,
    'daffodil'      ,
    'garlic_mustard'    ,
    'geranium'      ,
    'henbit'     ,
    'mullein'     ,
    'red_clover'    ,
]
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def main():
    return render_template("uploadpicture.html")

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        #print('upload_image filename: ' + filename)
        #flash('Image successfully uploaded and displayed below')

        # call predict to analyze the uploaded file
        new_image = predict.load_image(filepath)
        # check prediction
        pred = predict.model.predict(new_image)
        prediction = np.argmax(pred, axis=1)
        if prediction:
            prediction = FLOWER_TYPE[prediction[0]]

        return render_template('uploadpicture.html', filename=filename, prediction=prediction)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
 # PUT THE CODE FOR ANALYZING THE PICTURE HERE!!!
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.run(debug=True)
