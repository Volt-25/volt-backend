from flask import jsonify, request
from app.services import clubs_service

def get_all_clubs():
    try:
        data = clubs_service.get_all_clubs()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def add_club():
    try:
        club_data = request.get_json()
        club_id = clubs_service.create_club(club_data)
        return jsonify({'_id': str(club_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
