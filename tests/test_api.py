import unittest
import requests

class TestIrisAPI(unittest.TestCase):
    def test_prediction_endpoint(self):
        url = "http://localhost:5000/predict"
        payload = {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
        response = requests.post(url, json=payload)

        # Ensure the request succeeded
        self.assertEqual(response.status_code, 200)

        data = response.json()