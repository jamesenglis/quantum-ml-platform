#!/bin/bash

# Build and run Quantum ML Platform with Docker

set -e

echo "🚀 Building Quantum ML Platform Docker images..."

# Build the main API image
docker build -t quantum-ml-platform:latest .

echo "✅ Build complete!"

# Run with Docker Compose
echo "Starting services with Docker Compose..."
docker-compose up -d

echo "🎉 Services started!"
echo ""
echo "📊 Access your services:"
echo "   FastAPI: http://localhost:8000"
echo "   MLflow: http://localhost:5000" 
echo "   Prefect: http://localhost:4200"
echo ""
echo "🔍 Check service status: docker-compose ps"
echo "📝 View logs: docker-compose logs -f"
echo "🛑 Stop services: docker-compose down"
