from flask import Blueprint, jsonify, request
from app.controllers import events_controller

bp = Blueprint('events', __name__, url_prefix='/events')

@bp.route('/', methods=['GET'])
def get_all_data():
    return events_controller.get_all_data()

@bp.route('/', methods=['POST'])
def add_data():
    return events_controller.add_data()

@bp.route('/register', methods=['POST'])
def register_for_event():
    return events_controller.register_for_event()
