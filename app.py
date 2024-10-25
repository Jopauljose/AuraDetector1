from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Configuration: Replace with actual Gemini API endpoint and API key
GEMINI_API_URL = "https://api.gemini.com/v1/aura"  # Hypothetical endpoint
GEMINI_API_KEY = "your_gemini_api_key_here"  # API key if authentication is required

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate_aura', methods=['POST'])
def calculate_aura():
    scenario = request.form.get('scenario')

    if not scenario:
        return jsonify({"error": "No scenario provided"}), 400

    # Prepare the API call to Gemini
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "scenario": scenario
    }

    # Make the request to Gemini API
    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=data)
        response.raise_for_status()
        aura_data = response.json()

        # Extract aura result from response
        aura = aura_data.get("aura")
        if not aura:
            return jsonify({"error": "Failed to calculate aura"}), 500

        return render_template('result.html', aura=aura, scenario=scenario)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
