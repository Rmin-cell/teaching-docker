# Docker Workshop: Todo API Project

This repository contains a simple Flask Todo API project designed to teach Docker fundamentals in a hands-on, one-hour workshop.

## Prerequisites

- Basic understanding of command line interfaces
- Computer with Docker installed
  - [Docker Desktop](https://www.docker.com/products/docker-desktop) for Windows/Mac
  - [Docker Engine](https://docs.docker.com/engine/install/) for Linux

## Project Overview

This project demonstrates:
- Creating a Dockerfile for a Python application
- Building and running Docker containers
- Working with Docker registries
- Essential Docker commands for development

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/docker-todo-demo.git
cd docker-todo-demo
```

### 2. Project Structure

```
docker-todo-demo/
├── app.py                 # Flask API application
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker image definition
└── docker-compose.yml     # Docker Compose configuration (optional)
```

### 3. Building the Docker Image

```bash
docker build -t todo-api .
```

### 4. Running the Container

```bash
docker run -d -p 5000:5000 --name todo-container todo-api
```

### 5. Testing the API

The API will be available at http://localhost:5000

Endpoints:
- `GET /` - Welcome message
- `GET /todos` - List all todos
- `POST /todos` - Create a new todo

Example with curl:
```bash
# Get all todos
curl http://localhost:5000/todos

# Add a new todo
curl -X POST -H "Content-Type: application/json" -d '{"task":"Learn Docker"}' http://localhost:5000/todos
```

## Docker Commands Reference

### Basic Container Operations

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop todo-container

# Start a stopped container
docker start todo-container

# Remove a container (must be stopped first)
docker rm todo-container

# Remove a running container forcefully
docker rm -f todo-container

# View container logs
docker logs todo-container

# Execute command inside running container
docker exec -it todo-container /bin/bash
```

### Image Operations

```bash
# List all images
docker images

# Remove an image
docker rmi todo-api

# Pull an image from a registry
docker pull python:3.9-slim
```

### Working with Registries

```bash
# Log into a registry
docker login [registry-url]

# Tag an image for a registry
docker tag todo-api:latest [registry-url]/username/todo-api:latest

# Push an image to a registry
docker push [registry-url]/username/todo-api:latest

# Pull an image from a registry
docker pull [registry-url]/username/todo-api:latest

# Log out from a registry
docker logout [registry-url]
```

### Docker Compose (Optional)

```bash
# Start services defined in docker-compose.yml
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs
```

## Next Steps

After completing this workshop, explore:

1. Multi-container applications with Docker Compose
2. Docker networks and data persistence
3. Docker health checks and restart policies
4. Optimizing Docker images
5. CI/CD with Docker

## Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Flask Documentation](https://flask.palletsprojects.com/)