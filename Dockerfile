FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY lcm_service.py .

EXPOSE 10000

CMD ["python", "lcm_service.py"]