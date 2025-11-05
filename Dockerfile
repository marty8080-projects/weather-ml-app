FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code

# Run the app
CMD ["python3", "app.py"]
