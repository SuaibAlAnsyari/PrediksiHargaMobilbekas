import streamlit as st
import streamlit.components.v1 as stc

from flask import Flask, render_template, request
import pickle 

app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods = ["POST"])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    Mobil = (request.form['Mobil'])
    Tahun = (request.form['Tahun'])
    Jarak = int(request.form['Jarak'])
    Tipe = int(request.form['Tipe'])
    Gearbox = int(request.form['Gearbox'])
    BBM = int(request.form['BBM'])
    CC = int(request.form['CC'])
    Warna = int(request.form['Warna'])
    Kapasitas = int(request.form['Kapasitas'])
    

    predict_list = [[Mobil, Tahun, Jarak, Tipe, Gearbox, BBM, CC, Warna, Kapasitas]]
    prediction = model.predict(predict_list)
    output = round(prediction[0])

    return render_template('index.html', prediction_text='Harga Mobil Anda Adalah $ {} '.format(output))


if __name__ =="_main_":
    app.run(debug = True)
