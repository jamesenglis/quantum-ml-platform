#!/bin/bash

echo "🚀 Quantum ML Platform Quick Start"
echo "=================================="

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker Desktop first."
    echo "   Then run: open -a Docker"
    exit 1
fi

echo "✅ Docker is running"

# Build the image
echo "📦 Building Docker image..."
docker build -t quantum-ml-platform:latest .

# Start services
echo "🐳 Starting services with Docker Compose..."
docker-compose up -d

echo ""
echo "🎉 Quantum ML Platform is starting!"
echo ""
echo "📊 Services will be available at:"
echo "   • FastAPI: http://localhost:8000"
echo "   • MLflow: http://localhost:5000"
echo "   • Prefect: http://localhost:4200"
echo ""
echo "🔍 Check status: docker-compose ps"
echo "📝 View logs: docker-compose logs -f"
echo "🛑 Stop services: docker-compose down"
echo ""
echo "📚 API Documentation: http://localhost:8000/docs"
