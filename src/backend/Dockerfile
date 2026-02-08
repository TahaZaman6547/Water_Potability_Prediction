FROM python:3.11-slim

WORKDIR /app

# Copy root requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY src/backend /app/src/backend
COPY src/models /app/src/models

WORKDIR /app/src/backend

# Make script executable
RUN chmod +x start.sh

EXPOSE 8000

CMD ["bash", "start.sh"]