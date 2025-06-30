# Use official Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose FastAPI default port
EXPOSE 80

# Command to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]