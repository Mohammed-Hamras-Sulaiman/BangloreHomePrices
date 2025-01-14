from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify([
        'locations':util.get_location_names()
    ])

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(requests.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
        return.header.add('Access Control Allow Origin', '*')

        return response

if __name__ == "__main__":
    print("Starting python flask server for house price prediction....")
    app.run()