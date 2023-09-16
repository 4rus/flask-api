# Import necessary modules
from flask import Flask, jsonify, request
from data import data  # Assuming data is imported from another file

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL "/"
@app.route("/")
def index():
    # Return JSON response with data and a success message
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

# Define a route for "/star"
@app.route("/star")
def star():
    # Get the "name" query parameter from the request
    name = request.args.get("name")
    
    # Find the star data with a matching "name" in the data list
    star_data = next(item for item in data if item["name"] == name)
    
    # Return JSON response with the star data and a success message
    return jsonify({
        "data": star_data,
        "message": "success"
    }), 200

# Start the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run()
