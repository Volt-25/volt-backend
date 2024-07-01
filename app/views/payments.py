from flask import Blueprint, jsonify, request, redirect, url_for
from app.controllers import payments_controller

bp = Blueprint('payments', __name__, url_prefix='/payments')

@bp.route('/gateway', methods=['GET'])
def payment_gateway():
    return payments_controller.payment_gateway()

@bp.route('/', methods=['GET'])
def payment():
    return payments_controller.payment()
