FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create directory for temporary files
RUN mkdir -p /tmp/uploads

# Expose port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
