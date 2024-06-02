# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables to ensure non-root user can install packages
ENV PATH=/home/appuser/.local/bin:$PATH

# Create a non-root user
RUN useradd -m appuser

# Set the working directory to /app
WORKDIR /app

# Add the current directory contents into the container at /app
COPY --chown=appuser:appuser . /app

# Switch to non-root user
USER appuser

# Install any needed packages specified in requirements.txt
RUN pip install --user -e .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
