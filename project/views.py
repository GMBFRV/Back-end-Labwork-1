from flask import Flask, jsonify, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status = 'Service is up and running'
    greeting = 'Hello, user!'
    response_data = {
        'timestamp': current_time,
        'status': status,
        'greeting': greeting
    }
    return jsonify(response_data), 200

@app.route('/', methods=['GET'])
def welcome():
    return 'Welcome, user! <a href="/healthcheck">Go to Healthcheck</a>'

if __name__ == '__main__':
    app.run()
