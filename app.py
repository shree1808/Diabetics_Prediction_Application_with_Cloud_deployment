import numpy as np
import pickle
from flask import Flask,render_template,request

model = pickle.load(open('C:\\Users\\Shree123\\ML_end2end_EC2_AWS\\tuned_model.pkl','rb')) # read in binary mode
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict' , methods = ['POST'])
def predict_outcome():
    pregnancies = int(request.form.get('pregnancies'))
    glucose = int(request.form.get('glucose'))
    blood_pressure = int(request.form.get('blood_pressure'))
    skin_thickness = int(request.form.get('skin_thickness'))
    insulin = int(request.form.get('insulin'))
    bmi = float(request.form.get('bmi'))
    diabetes_pedigree_function = float(request.form.get('diabetes_pedigree_function'))
    age = int(request.form.get('age'))

    input_array = np.array([pregnancies, glucose, blood_pressure, skin_thickness,
                                insulin, bmi, diabetes_pedigree_function, age]).reshape(1, 8)

    prediction = model.predict(input_array)

    if prediction[0] == 1:
        prediction = 'Diabetic'
    else:
        prediction = 'not Diabetic'

    return render_template('index.html',result= prediction) 

    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)

    

