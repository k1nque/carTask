FROM python:3.10

ENV PYTHONBUFFERED=1

WORKDIR /car_api

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
