from flask import jsonify, request, redirect, url_for
from app.services import payments_service

def payment_gateway():
    try:
        athlete_id = request.args.get('athlete_id')
        event_id = request.args.get('event_id')
        redirect_url = payments_service.get_payment_gateway_url(athlete_id, event_id)
        return redirect(redirect_url)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def payment():
    try:
        return payments_service.render_payment_page()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
