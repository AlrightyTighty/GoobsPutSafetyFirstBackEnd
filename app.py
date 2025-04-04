from flask import Flask, request
import requests

API_KEY = "f6d1b4dbacc4354090a9504d91db369d" # change this to be an environment variable

app = Flask(__name__)

@app.route("/flight-info", methods=['POST', 'GET'])
def get_flight_info():
    flight_number = request.args.get('flightnum')
    res = requests.get("https://api.aviationstack.com/v1/flights?access_key="+API_KEY+"&flight_number="+flight_number)
    print(res.json())
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)