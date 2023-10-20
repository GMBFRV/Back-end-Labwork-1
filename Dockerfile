FROM python:3.11.3

WORKDIR /project

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /project

CMD flask --app <your app name> run -h 0.0.0.0 -p $PORT