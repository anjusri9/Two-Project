import unittest
import requests

class TestIrisAPI(unittest.TestCase):
    def test_prediction_endpoint(self):
        url = "http://localhost:5000/predict"
        payload = {
            "sepal_length": 7.5,
            "sepal_width": 8.3,
            "petal_length": 5.4,
            "petal_width": 12.9
        }
        response = requests.post(url, json=payload)

        # Ensure the request succeeded
        self.assertEqual(response.status_code, 200)

        data = response.json()