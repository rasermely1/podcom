import unittest
from flask import Flask, jsonify, request
from query import query  # Import the query function from your module
from unittest.mock import patch, MagicMock

# Create a Flask app for testing
app = Flask(__name__)

# Register the route for the query function
@app.route('/query', methods=['POST'])
def query_route():
    return query()

class QueryFunctionTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    @patch('your_module.text_query_engine')
    def test_query_function(self, mock_text_query_engine):
        # Mock the text_query_engine.query method
        mock_text_query_engine.query.return_value = "Mocked query result"

        # Create a test request
        test_data = {'query': 'test query'}
        response = self.app.post('/query', json=test_data)

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the response data
        response_data = response.get_json()
        expected_data = {"results": "Mocked query result"}
        self.assertEqual(response_data, expected_data)

if __name__ == '__main__':
    unittest.main()
