from flask import Flask, render_template, request
import google.generativeai as genai

# Initialize the Flask application
app = Flask("AuraCalculator1")

# Configure the Gemini API with your API key
genai.configure(api_key="AIzaSyCKXQyrywDc4J9jacv4q1cGkhWkAV0-KpI")
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to calculate aura based on the user's scenario input
def calculate_aura(scenario):
    try:
        # Construct a query to generate an aura score
        query = f"Provide an aura score from -10000 to 10000 based on this scenario: {scenario}"
        
        # Generate content using the Gemini model
        response = model.generate_content(query)
        
        # Extract the text output
        aura_score_text = response.text
        
        # Parse the output into an integer if possible, defaulting to 0 on error
        try:
            aura_score = int(aura_score_text)
        except ValueError:
            aura_score = 0  # Handle unexpected non-numeric responses

        return aura_score
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve the scenario input from the form
        scenario = request.form.get("scenario")
        if scenario:
            # Calculate the aura score based on the scenario
            aura_score = calculate_aura(scenario)
            return render_template("index.html", aura_score=aura_score)
        else:
            return render_template("index.html", error="Please enter a valid scenario.")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
v
