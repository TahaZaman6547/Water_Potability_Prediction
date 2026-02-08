FROM python:3.11-slim

WORKDIR /app

# Copy root requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend code
COPY src/frontend /app/src/frontend

WORKDIR /app/src/frontend

# Make script executable
RUN chmod +x start.sh

EXPOSE 8501

CMD ["bash", "start.sh"]
