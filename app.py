from flask import Flask, request, jsonify
import requests
from uuid import uuid4
import os

app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return 'Hello, world!'

# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
