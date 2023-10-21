FROM python:3.10

WORKDIR /backend

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "project/views.py"]