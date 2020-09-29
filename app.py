from flask import Flask, request, jsonify
import numpy as np
import pickle
import pandas as pd

app=Flask(__name__)
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


@app.route('/')
def welcome():
    return "Welcome All"
  
"""
@app.route('/predict', methods=['Post'])
def predict_note_authentication():
  variance = float(request.form['variance'])
  skewness = float(request.form['skewness'])
  curtosis = float(request.form['curtosis'])
  entropy = float(request.form['entropy'])
  
  prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
  
  return "prediction is"+ str(prediction)
"""

@app.route('/predict')
def predict_note_authentication():
  variance = request.args.get('variance')
  skewness = request.args.get('skewness')
  curtosis = request.args.get('curtosis')
  entropy = request.args.get('entropy')
  prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
  return "The prediction value is " + str(prediction) 
  # http://127.0.0.1:5000/predict?variance=1&skewness=2&curtosis=3&entropy=2 

@app.route('/predict_file', methods=["POST"])
def predict_note_file():
  df_test = pd.read_csv(request.files.get("file"))
  prediction = classifier.predict(df_test)
  return "The prediction value for the csv is " + str(list(prediction))

if __name__=='__main__':
    app.run()
