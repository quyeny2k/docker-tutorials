FROM python:3.12-slim

WORKDIR /code

COPY ops.py .
COPY requirements.txt .
COPY tests ./tests
RUN pip install --upgrade pip
#RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
CMD ["python", "ops.py"]
#CMD ["python", "-m", "pytest", "-v", "tests"]
#CMD ["sleep", "300"]