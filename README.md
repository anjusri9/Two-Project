# Iris MLOps Microservice

## Model Training
```bash
python model/train.py
```

## Run API Locally
```bash
docker build -t iris-api:1.0.0 .
docker run -p 5000:5000 iris-api:1.0.0
```

## Testing the microservice (can use curl or postman to send request)
```bash
curl -X POST http://localhost:5000/predict \
 -H "Content-Type: application/json" \
 -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'

Invoke-RestMethod -Uri http://localhost:5000/predict `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{ "sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2 }'
```

## Infrastructure
```bash
cd terraform
terraform init
terraform apply
```

## CI/CD
- GitHub Actions for test/build steps

## Design Decisions
Flask was chosen for its simplicity in exposing a lightweight ML model as a REST API.
Scikit-learn Pipeline ensures preprocessing and model are bundled together, preventing train–serve skew.
Docker provides consistent, portable environments across development and deployment.
Terraform automates cloud infrastructure provisioning in a reproducible, scalable way.
GitHub Actions enables CI for testing and building on each code push.
Versioning is handled via artifact (model_pipeline.joblib) and Docker image tags (e.g., :1.0.0).