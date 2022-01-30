from flask import Flask, jsonify, request
import pickle
import numpy as np

model = pickle.load(open('finalized_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

column_order = ['Age', 'FastingBS', 'Oldpeak', 'Sex_F', 'ExerciseAngina_Y', 'ST_Slope_Down', 'ST_Slope_Flat', 'ChestPainType_ASY_ChestPainType_ATA_ChestPainType_NAP']

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = request.json

    X = [data[col] for col in column_order]
    X = np.array(X)
    X = X.reshape(len(X), 1)
    test = scaler.transform([[X[0], 0, 0, 0, X[2]]])
    X[0] = test[0, 0]
    X[2] = test[0, 4]
    new_X = X.T
    prediction = model.predict(new_X)[0]
    return jsonify({"prediction" : str(prediction)})

app.run()