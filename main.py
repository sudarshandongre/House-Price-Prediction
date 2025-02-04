# flask, scikit-learn, pandas, pickle-num, numpy
from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
app = Flask(__name__)
data = pd.read_csv("./DataSet/Cleaned_data.csv")
pipe = pickle.load(open('Model.pkl', 'rb'))

@app.route("/")
def index():
    locations = sorted(data['Address'].unique())
    status = sorted(data['Status'].unique())
    new_or_old = sorted(data['neworold'].unique())
    type_of_building = sorted(data['type_of_building'].unique())
    return render_template('index.html', locations=locations, status = status, new_or_old = new_or_old, type_of_building = type_of_building)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    status = request.form.get('status')
    new_old = request.form.get('new_old')
    type_building = request.form.get('type_building')
    bhk = request.form.get('bhk')
    bath = request.form.get('Bathrooms')
    bed = request.form.get('Bedrooms')
    sqft = request.form.get('area')
    print(location,sqft,bath,bhk,status,new_old,type_building)
    input = pd.DataFrame([[location,sqft,bath,bed,bhk,status,new_old,type_building]],columns=['Address', 'area', 'Bathrooms', 'Bedrooms', 'bhk', 'Status', 'neworold', 'type_of_building'])
    print(input)
    prediction = pipe.predict(input)[0] * 1e5
    return str(np.round(prediction, 2)) 
    

if __name__ == "__main__":
    app.run(debug=True,port=3000)
