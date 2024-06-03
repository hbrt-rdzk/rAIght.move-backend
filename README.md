# rAIght.move-backend

FastAPI backend with endpoints for explaining mistakes during exercise performance.

## About

This project is a backend service built with FastAPI to provide insights and explanations for mistakes made during exercise performance. It aims to help users improve their exercise routines by offering detailed feedback.

## Features

- FastAPI framework for high performance
- Endpoints to analyze and explain exercise mistakes
- Dockerfile for containerized deployment

## Requirements

- Python 3.11+
- FastAPI
- Docker (optional, for containerized deployment)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hbrt-rdzk/rAIght.move-backend.git
   cd rAIght.move-backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -e .
   ```

## Usage

1. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`

## Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t raight-move-backend .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 raight-move-backend
   ```

## Project Structure

- `app/` - Contains the FastAPI application and endpoints
- `configs/` - Configuration files
- `data/` - Data files for the application
- `.gitignore` - Git ignore file
- `Dockerfile` - Dockerfile for containerization
- `pyproject.toml` - Project configuration file
- `README.md` - Project documentation

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any changes.
