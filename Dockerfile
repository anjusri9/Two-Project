FROM python:3.10-slim
WORKDIR /app
COPY model/model_pipeline.joblib model/model_pipeline.joblib
COPY app/ app/
RUN pip install --no-cache-dir -r app/requirements.txt
EXPOSE 5000
CMD ["python", "app/main.py"]
