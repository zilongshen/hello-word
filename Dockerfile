# Use Python 3.10 slim as the base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port 8000
EXPOSE 8000

# # Command to run the application
# CMD ["chroma", "run", "--host", "0.0.0.0", "--path", "/chroma/data"]
CMD ["python", "src/hello_world/main.py"]