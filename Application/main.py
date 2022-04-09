'''This file contains code for main application built using Flask'''

import pandas as pd



from flask import Flask, request, jsonify

def value_prediction(year,month):
    datafile    = pd.read_csv("Final_Values.csv", index_col=False)
    predictions = datafile.loc[lambda datafile: datafile['JAHR'] == year].loc[lambda datafile: datafile['MONTH'] == month]
    return predictions.iloc[0]['FINAL_VALUES']

app = Flask(__name__)

@app.route("/prediction", methods=['GET','POST'])
def index():
    data = request.get_json()
    year = data['year']
    month = data['month']

    prediction = value_prediction(year, month)

    return jsonify({"prediction": int(prediction)})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)