FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app.py .

EXPOSE 8000

CMD ["fastapi", "run", "app.py", "--port", "8000"]
