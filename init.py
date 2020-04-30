#!/usr/bin/python3
import json
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def hello():
    return "hello world!"


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5100,
    )
