from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"



# Skip to content
# Search or jump to…
# Pull requests
# Issues
# Marketplace
# Explore
 
# @Linasaindane 
# siddharaj-jawalkar25
# /
# flask-application-interface
# Public
# Code
# Issues
# Pull requests
# Actions
# Projects
# Security
# Insights
# flask-application-interface/main.py /
# @siddharaj-jawalkar25
# siddharaj-jawalkar25 Working code is successfully uploaded
# Latest commit 0876480 on 19 May
#  History
#  1 contributor
# 47 lines (39 sloc)  1.49 KB

import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['pdf', 'txt', 'docx', 'jpg', 'png'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No file selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		flash('File successfully uploaded and displayed below')
		return render_template('upload.html', filename=filename)
	else:
		flash('Allowed image types are -> pdf, txt, docx, jpg, png')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_file(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
You have no unread notifications    