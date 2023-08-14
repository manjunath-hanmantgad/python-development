import random
import logging
import pytest
from flask import Flask, request, jsonify
import pandera as pa

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
        schema = pa.DataFrameSchema({
            "sentence": pa.Column(pa.String)
        })
        schema(data)  # Validate the JSON data using the defined schema

        sentence = data.get('sentence')  # Extract the 'sentence' value from JSON data

        if not isinstance(sentence, str):
            raise ValueError('Invalid input. Expected a sentence as a string.')

        result = generate_random_array(sentence)  # Generate the random array
        return jsonify(result)  # Return the random array as a JSON response

    except pa.errors.SchemaError as se:  # Updated from SchemaErrors to SchemaError
        # If the input JSON does not match the schema, return a 400 error with validation errors
        return jsonify({'error': str(se)}), 400

    except ValueError as ve:
        # If the input sentence is not a string, return a 400 error with an error message
        return jsonify({'error': str(ve)}), 400

    except Exception as e:
        # Log the error and return a 500 response
        error_msg = f'Internal server error: {e}'
        logging.error(error_msg)
        # For any other unexpected error, return a 500 error with an error message
        return jsonify({'error': 'Internal server error.'}), 500

def test_generate_array_success():
    # Test the /generate_array endpoint with a valid input
    data = {"sentence": "This is an example sentence"}
    response = app.test_client().post('/generate_array', json=data)

    assert response.status_code == 200
    result = response.get_json()
    assert isinstance(result, list)
    assert len(result) == 500
    assert all(isinstance(num, float) for num in result)

def test_generate_array_invalid_input():
    # Test the /generate_array endpoint with an invalid input (non-string)
    data = {"sentence": 123}
    response = app.test_client().post('/generate_array', json=data)

    assert response.status_code == 400
    result = response.get_json()
    assert 'error' in result

if __name__ == '__main__':
    pytest.main()
