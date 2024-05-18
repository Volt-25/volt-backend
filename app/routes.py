from flask import request, jsonify
from app import app
from app.controllers import EventController, ClubController

@app.route('/')
def hello_world():
    return 'Hello, VOLT!'

@app.route('/data', methods=['GET'])
def get_all_data():
    return EventController.get_all_events()

@app.route('/data', methods=['POST'])
def add_data():
    return EventController.add_event(request.get_json())

@app.route('/clubs', methods=['GET'])
def get_all_clubs():
    return ClubController.get_all_clubs()

@app.route('/clubs', methods=['POST'])
def add_club():
    return ClubController.add_club(request.get_json())
