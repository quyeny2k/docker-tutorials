FROM python:3.12-slim

WORKDIR /code

COPY src .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

CMD ["python", "-m", "pytest", "-v", "tests/test_ops.py"]
