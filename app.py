import joblib
import numpy
from flask import Flask, request
from sklearn import *

MODEL1_PATH = "for_models/model_forest.pkl"
SCALER1_X_PATH = "for_models/scaler_x_forest.pkl"
SCALER1_Y_PATH = "for_models/scaler_y_forest.pkl"

MODEL2_PATH = "for_models/model_catboost.pkl"
SCALER2_X_PATH = "for_models/scaler_x_catboost.pkl"
SCALER2_Y_PATH = "for_models/scaler_y_catboost.pkl"


app = Flask(__name__)
model1 = joblib.load(MODEL1_PATH)
sc1_x = joblib.load(SCALER1_X_PATH)
sc1_y = joblib.load(SCALER1_Y_PATH)

model2 = joblib.load(MODEL2_PATH)
sc2_x = joblib.load(SCALER2_X_PATH)
sc2_y = joblib.load(SCALER2_Y_PATH)

@app.route("/predict_price", methods=['GET'])
def predict():

    args = request.args
    modeltype = args.get('modeltype', default=-1, type=int)
    rooms = args.get('rooms', default=-1, type=int)
    area = args.get('area', default=-1, type=float)
    renovation = args.get('renovation', default=-1,type=int)
    amount = args.get('amount', default=-1, type=int)

    if modeltype==1:
        x = numpy.array([rooms, area, renovation,amount]).reshape(1,-1)
        x = sc1_x.transform(x)
        result = model1.predict(x)
        result = sc1_y.inverse_transform(result.reshape(1,-1))

        return str(result[0][0])

    elif modeltype == 2:
        x = numpy.array([rooms, area, renovation, amount]).reshape(1, -1)
        x = sc2_x.transform(x)
        result = model2.predict(x)
        result = sc2_y.inverse_transform(result.reshape(1, -1))

        return str(result[0][0])


if __name__=='__main__':
    app.run(debug=True, port=5444, host='0.0.0.0')
