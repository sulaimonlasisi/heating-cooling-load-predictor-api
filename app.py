import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=UserWarning)
    import pandas as pd
from flask import Flask, jsonify, request
from joblib import load

# load model
linear_reg_model = load('linear_reg.joblib')

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = linear_reg_model.predict(data_df)

    # send back to browser
    output = {'Heating Load': round(result[0][0], 2), 'Cooling Load': round(result[0][1], 2)}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True, host='0.0.0.0')
