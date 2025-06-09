# Docker Compose Application: User Management System

This repository contains a containerized application that includes a Python FastAPI backend and a Vue.js frontend. The application demonstrates a simple user management system with CRUD operations.

## Architecture

The application consists of two main services:

### Backend Service

- **Technology**: Python with FastAPI
- **Purpose**: Provides a RESTful API for user management
- **Endpoints**: CRUD operations for users
- **Container**: Python 3.13 slim image
- **Port**: 8000

### Frontend Service

- **Technology**: Vue.js with TypeScript
- **Purpose**: Web interface for user management
- **Features**: Create, Read, Update, Delete users
- **Container**: Multi-stage build using Node.js for building and Nginx for serving
- **Port**: 80

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Running the Application

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd docker-praktikum
   ```

2. Start the services using Docker Compose:

   ```bash
   cd examples
   docker-compose up -d
   ```

3. Access the application:
   - Frontend: http://localhost
   - Backend API: http://localhost:8000

## Features

The application provides a web interface for:

- Listing all users
- Creating new users
- Retrieving user details by ID
- Updating existing user information
- Deleting users

## API Endpoints

The backend provides the following API endpoints:

- `GET /users` - List all users
- `GET /users/{id}` - Get user by ID
- `POST /users` - Create a new user
- `PUT /users/{id}` - Update a user
- `DELETE /users/{id}` - Delete a user

## Development

### Frontend Development

The Vue.js frontend is located in the [`examples/vuejs`](examples/vuejs) directory.

```bash
cd examples/vuejs
pnpm install
pnpm dev
```

See the Vue.js README for more information.

### Backend Development

The Python backend is located in the [`examples/python`](examples/python) directory.

```bash
cd examples/python
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Docker Configuration

The application uses Docker Compose to orchestrate two containers:

1. **Backend Container**:

   - Built from the Python 3.13 slim image
   - Installs dependencies from requirements.txt
   - Exposes port 8000

2. **Frontend Container**:
   - Uses a multi-stage build:
     - Build stage: Node.js to compile and build the Vue application
     - Production stage: Nginx to serve the static files
   - Configured to proxy API requests to the backend
   - Exposes port 80

## License

[License information goes here]
