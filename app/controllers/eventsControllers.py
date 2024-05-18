from flask import jsonify
from app.models import events_collection, clubs_collection

class EventController:
    @staticmethod
    def get_all_events():
        try:
            data = list(events_collection.find({}))
            for item in data:
                item['_id'] = str(item['_id'])
            return jsonify(data), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def add_event(event_data):
        try:
            event_name = event_data.get('Eventname')
            event_description = event_data.get('Eventdescription')
            sport_name = event_data.get('Sportname')
            event_organizer = event_data.get('Eventorganizer')
            event_cost = event_data.get('Eventcost')
            event_date = event_data.get('Eventdate')
            event_location = event_data.get('Eventlocation')

            if not all([event_name, event_description, sport_name, event_organizer, event_cost, event_date, event_location]):
                return jsonify({'error': 'Missing required fields'}), 400

            new_event = {
                'Eventname': event_name,
                'Eventdescription': event_description,
                'Sportname': sport_name,
                'Eventorganizer': event_organizer,
                'Eventcost': event_cost,
                'Eventdate': event_date,
                'Eventlocation': event_location
            }

            result = events_collection.insert_one(new_event)
            return jsonify({'_id': str(result.inserted_id)}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

class ClubController:
    @staticmethod
    def get_all_clubs():
        try:
            data = list(clubs_collection.find({}))
            for item in data:
                item['_id'] = str(item['_id'])
            return jsonify(data), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def add_club(club_data):
        try:
            club_name = club_data.get('Clubname')
            club_description = club_data.get('Clubdescription')
            sport_name = club_data.get('Sportname')
            club_organizer = club_data.get('Cluborganizer')
            club_location = club_data.get('Clublocation')

            if not all([club_name, club_description, sport_name, club_organizer, club_location]):
                return jsonify({'error': 'Missing required fields'}), 400

            new_club = {
                'Clubname': club_name,
                'Clubdescription': club_description,
                'Sportname': sport_name,
                'Cluborganizer': club_organizer,
                'Clublocation': club_location
            }

            result = clubs_collection.insert_one(new_club)
            return jsonify({'_id': str(result.inserted_id)}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
