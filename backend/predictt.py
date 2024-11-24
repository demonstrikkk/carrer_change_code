from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)
from flask_cors import CORS
CORS(app)  # Enable Cross-Origin Resource Sharing for all domains (modify as needed)

# Load the pre-trained model (make sure to update the path to your model)
model = joblib.load('/carrer_change_code\\backend\\best_model21.pkl')

# # Test route to verify the server is working
# @app.route('/test', methods=['GET'])
# def test():
#     return jsonify({"message": "Flask is running properly!"})
#
# # Test route to verify POST requests
# @app.route('/test-post', methods=['POST'])
# def test_post():
#     data = request.json  # Get the JSON payload from the frontend
#     print('Received POST Data:', data)  # Log the received data
#     return jsonify({
#         "received_data": data,
#         "message": "POST request successful!"
#     })
#
# Main route to render the form
@app.route('/')
def home():
    return render_template('form.html')

# Favicon route to avoid 404 errors for favicon requests
@app.route('/favicon.ico')
def favicon():
    return '', 204

# Prediction route (Main Prediction Endpoint)
@app.route('/predict', methods=['POST'])
def predict():
    expected_fields = [
        'Field of Study', 'Current Occupation', 'Age', 'Gender', 'Years of Experience',
        'Education Level', 'Industry Growth Rate', 'Job Satisfaction',
        'Work-Life Balance', 'Job Opportunities', 'Job Security', 'Career Change Interest',
        'Skills Gap', 'Family Influence', 'Mentorship Available', 'Certifications',
        'Freelancing Experience', 'Geographic Mobility', 'Professional Networks',
        'Technology Adoption', 'Salary Group'
    ]

    try:
        data = request.json  # Get JSON data from the frontend
        print('Received Data:', data)  # Log the received data for debugging

        # Check if all expected fields are present in the incoming data
        missing_fields = [field for field in expected_fields if field not in data]
        if missing_fields:
            print(f'Missing fields: {missing_fields}')
            return jsonify({'error': f'Missing fields: {", ".join(missing_fields)}'}), 400

        # Assuming 'data' is a dictionary of field names and values
        input_data = pd.DataFrame([data])
        prediction = model.predict(input_data)[0]  # Get prediction
        if int(prediction) ==0:
            predict_str = 'No'
        else:
            predict_str ='Yes'
        print('Prediction:', prediction)  # Log prediction for debugging
        return jsonify({'prediction': predict_str})

    except Exception as e:
        # Log the error message and return a 400 error response with the error message
        print(f'Error occurred: {str(e)}')
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)

