FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y build-essential && apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Expose Streamlit (8501) and FastAPI (8000) ports
EXPOSE 8000
EXPOSE 8501

# Run both FastAPI and Streamlit using bash script
CMD ["bash", "-c", "uvicorn backend:app --host 0.0.0.0 --port 8000 & streamlit run frontend.py --server.port=8501 --server.address=0.0.0.0"]
