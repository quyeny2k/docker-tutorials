FROM python:3.12-slim

WORKDIR /example2

COPY requirements.txt /example2/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /example2/requirements.txt

COPY ./app  /example2/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]