from flask import Flask, request, jsonify
import joblib
import uuid

app = Flask(__name__)
model = joblib.load("model/model_pipeline.joblib")

species = ['setosa', 'versicolor', 'virginica']

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = [[
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]]
    prediction = model.predict(features)[0]
    response = {
        "prediction": int(prediction),
        "prediction_label": species[prediction],
        "request_id": str(uuid.uuid4()),
        "model_version": "1.0.0"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)