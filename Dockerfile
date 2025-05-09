# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy all project files
COPY . .

# Run Django development server
CMD ["python", "ToDo/manage.py", "runserver", "0.0.0.0:5000", "--noreload"]
