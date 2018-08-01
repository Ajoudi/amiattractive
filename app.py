from flask import Flask, render_template,request
import re
import base64
from scipy.misc import imread
from load import * 
import numpy as np
global model, graph
import os

model, graph = init()


app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = 'static'


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
    
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/imgsave',methods=['POST'])
def upload_file():
	f = request.files['image']
	f.save(os.path.join(app.config['UPLOAD_FOLDER'], 'output.jpg'))
	return render_template('predict.html') 

@app.route('/predict/',methods=['GET','POST'])
def predict():
	x = imread('static/output.jpg')
	x1,x2,x3 = x.shape
	x = x.reshape(1,x1,x2,x3)
	print ("debug2")
	print(x)
	with graph.as_default():
		out = model.predict(x)
		print(out)
		print ("debug3")
		response = str(out)
		return response

if __name__ == "__main__":
	app.run(debug=True, port=33507)



