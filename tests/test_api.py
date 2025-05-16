import requests

data = {
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

response = requests.post("http://localhost:5000/predict", json=data)
print(response.json())
