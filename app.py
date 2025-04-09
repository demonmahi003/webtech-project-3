from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to access the backend

WEATHER_API_KEY = "52a3335680494d8c8b9125854252903"

@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')
    if not location:
        return jsonify({"error": "Location parameter missing"}), 400

    api_url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}&aqi=yes"
    response = requests.get(api_url)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather"}), 500

    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
