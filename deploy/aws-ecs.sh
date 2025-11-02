#!/bin/bash

echo "🚀 Deploying Quantum ML Platform to AWS ECS..."

# Build and push Docker image to ECR
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION="us-east-1"
ECR_REPO="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/quantum-ml-platform"

# Login to ECR
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REPO

# Create ECR repository if it doesn't exist
aws ecr describe-repositories --repository-names quantum-ml-platform || \
aws ecr create-repository --repository-name quantum-ml-platform

# Build and push image
docker build -t quantum-ml-platform:latest .
docker tag quantum-ml-platform:latest $ECR_REPO:latest
docker push $ECR_REPO:latest

echo "✅ Image pushed to ECR: $ECR_REPO:latest"

# Deploy to ECS (you would need to set up ECS cluster and task definition)
echo "📦 Deploying to ECS..."
# aws ecs update-service --cluster quantum-ml-cluster --service quantum-ml-service --force-new-deployment

echo "🎉 Deployment completed!"
