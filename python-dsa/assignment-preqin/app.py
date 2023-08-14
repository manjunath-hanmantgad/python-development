import random
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)  # Create a Flask application instance

# Set up error logging
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s: %(message)s')

def generate_random_array(sentence):
    """
    Function to generate a random 500-dimensional array of floats.

    Parameters:
        sentence (str): The input sentence.

    Returns:
        list: A random 500-dimensional array of floats.
    """
    # Replace this with your custom logic to generate the 500-dimensional array
    random_array = [random.uniform(0, 1) for _ in range(500)]
    return random_array

@app.route('/generate_array', methods=['POST'])
def generate_array():
    """
    Flask route to handle the POST request for generating the random array.

    Expects JSON data with 'sentence' key containing the input sentence.

    Returns:
        JSON: A JSON response containing the random 500-dimensional array
              or an error message if the input is invalid or server error occurs.
    """
    try:
        data = request.get_json()  # Get the JSON data from the request body
        sentence = data.get('sentence')  # Extract the 'sentence' value from JSON data

        if not isinstance(sentence, str):
            raise ValueError('Invalid input. Expected a sentence as a string.')

        result = generate_random_array(sentence)  # Generate the random array
        return jsonify(result)  # Return the random array as a JSON response

    except ValueError as ve:
        # If the input sentence is not a string, return a 400 error with an error message
        return jsonify({'error': str(ve)}), 400

    except Exception as e:
        # Log the error and return a 500 response
        error_msg = f'Internal server error: {e}'
        logging.error(error_msg)
        # For any other unexpected error, return a 500 error with an error message
        return jsonify({'error': 'Internal server error.'}), 500

if __name__ == '__main__':
    # Start the Flask development server if this script is executed directly
    app.run(host='0.0.0.0', port=5000)
