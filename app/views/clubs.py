from flask import Blueprint, jsonify, request
from app.controllers import clubs_controller

bp = Blueprint('clubs', __name__, url_prefix='/clubs')

@bp.route('/', methods=['GET'])
def get_all_clubs():
    return clubs_controller.get_all_clubs()

@bp.route('/', methods=['POST'])
def add_club():
    return clubs_controller.add_club()
