from flask import Flask, request
import requests

API_KEY = "f6d1b4dbacc4354090a9504d91db369d" # change this to be an environment variable

app = Flask(__name__)

@app.route("/flight-info", methods=['GET'])
def get_flight_info():
    flight_code = request.args.get('flightcode')
    res = requests.get("https://api.aviationstack.com/v1/flights?access_key="+API_KEY+"&flight_iata="+flight_code)
    print(res.json())
    return res.json()['data'][0]

if __name__ == "__main__":
    app.run(debug=True)