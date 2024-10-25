from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Gemini API configuration
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
GEMINI_API_KEY = "AIzaSyCKXQyrywDc4J9jacv4q1cGkhWkAV0-KpI"  # Replace with actual API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate_aura', methods=['POST'])
def calculate_aura():
    scenario = request.json.get('scenario')

    if not scenario:
        return jsonify({"error": "No scenario provided"}), 400

    # Prepare the API call to Gemini
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": scenario}
                ]
            }
        ]
    }

    # Make the request to the Gemini API
    try:
        response = requests.post(f"{AIzaSyCKXQyrywDc4J9jacv4q1cGkhWkAV0-KpI}?key={AIzaSyCKXQyrywDc4J9jacv4q1cGkhWkAV0-KpI}", headers=headers, json=data)
        response.raise_for_status()
        aura_data = response.json()

        # Extract aura result from the response (assuming 'aura' is in the response)
        aura = aura_data.get("aura")  # Adjust according to actual response structure
        if not aura:
            return jsonify({"error": "Failed to calculate aura"}), 500

        return jsonify({"aura": aura})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
