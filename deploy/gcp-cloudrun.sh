#!/bin/bash

echo "🚀 Deploying Quantum ML Platform to Google Cloud Run..."

PROJECT_ID="your-project-id"
SERVICE_NAME="quantum-ml-platform"
REGION="us-central1"

# Build and push to Google Container Registry
docker build -t gcr.io/$PROJECT_ID/$SERVICE_NAME:latest .

# Push to GCR
docker push gcr.io/$PROJECT_ID/$SERVICE_NAME:latest

# Deploy to Cloud Run
gcloud run deploy $SERVICE_NAME \
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME:latest \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --memory 1Gi \
  --cpu 1 \
  --concurrency 80 \
  --min-instances 1 \
  --max-instances 10

echo "🎉 Cloud Run deployment completed!"
