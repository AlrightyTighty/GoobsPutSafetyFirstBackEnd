from flask import Flask, request
from flask_cors import CORS, cross_origin
import requests
import os

API_KEY = os.getenv("FLIGHT_API_KEY") 

app = Flask(__name__)
cors = CORS(app)

@app.route("/flight-info", methods=['GET'])
@cross_origin()
def get_flight_info():
    flight_code = request.args.get('flightcode')
    res = requests.get("https://api.aviationstack.com/v1/flights?access_key="+API_KEY+"&flight_iata="+flight_code)
    print(res.json())
    return res.json()['data'][0]

if __name__ == "__main__":
    app.run(debug=True)