from flask import Flask, jsonify
from datetime import datetime
import os  # Добавляем импорт модуля os

app = Flask(__name__)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status = 'Service is up and running, code 200'
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
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))
