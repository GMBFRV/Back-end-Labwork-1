FROM python:3.10.10

WORKDIR /project

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /views

CMD flask --app views.py run -h 0.0.0.0 -p $PORT
