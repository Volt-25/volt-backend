from flask import jsonify, request, redirect, url_for
from bson.objectid import ObjectId
from app.services import events_service

def get_all_data():
    try:
        data = events_service.get_all_events()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def add_data():
    try:
        event_data = request.get_json()
        event_id = events_service.create_event(event_data)
        return jsonify({'_id': str(event_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def register_for_event():
    try:
        registration_data = request.get_json()
        redirect_url = events_service.register_for_event(registration_data)
        return redirect(redirect_url)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
