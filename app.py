from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId  # To handle MongoDB ObjectIds

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, VOLT!'

# MongoDB connection setup
client = MongoClient('mongodb+srv://theplasma:Plasma[][][][][]@theplasma.flv6npg.mongodb.net/?retryWrites=true&w=majority&appName=thePlasma')  # Update with your MongoDB URI if different
db = client['Volt']  # Replace with your database name
events_collection = db['Events']  # Replace with your collection name for events
clubs_collection = db['Clubs']  # Replace with your collection name for clubs

@app.route('/events', methods=['GET'])
def get_all_data():
    try:
        # Fetch all documents from the Events collection
        data = list(events_collection.find({}))
        
        # Convert ObjectId to string for JSON serialization
        for item in data:
            item['_id'] = str(item['_id'])
        
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/events', methods=['POST'])
def add_data():
    try:
        # Extract data from request
        event_data = request.get_json()
        
        # Validate and extract individual fields
        event_name = event_data.get('Eventname')
        event_description = event_data.get('Eventdescription')
        sport_name = event_data.get('Sportname')
        event_organizer = event_data.get('Eventorganizer')
        event_cost = event_data.get('Eventcost')
        event_date = event_data.get('Eventdate')
        event_location = event_data.get('Eventlocation')

        # Ensure all required fields are present
        if not all([event_name, event_description, sport_name, event_organizer, event_cost, event_date, event_location]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Prepare the document to insert
        new_event = {
            'Eventname': event_name,
            'Eventdescription': event_description,
            'Sportname': sport_name,
            'Eventorganizer': event_organizer,
            'Eventcost': event_cost,
            'Eventdate': event_date,
            'Eventlocation': event_location
        }
        
        # Insert the new document into the Events collection
        result = events_collection.insert_one(new_event)
        
        # Return the id of the new document
        return jsonify({'_id': str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to get all clubs
@app.route('/clubs', methods=['GET'])
def get_all_clubs():
    try:
        # Fetch all documents from the Clubs collection
        data = list(clubs_collection.find({}))
        
        # Convert ObjectId to string for JSON serialization
        for item in data:
            item['_id'] = str(item['_id'])
        
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to add a new club
@app.route('/clubs', methods=['POST'])
def add_club():
    try:
        # Extract data from request
        club_data = request.get_json()
        
        # Validate and extract individual fields
        club_name = club_data.get('Clubname')
        club_description = club_data.get('Clubdescription')
        sport_name = club_data.get('Sportname')
        club_organizer = club_data.get('Cluborganizer')
        club_location = club_data.get('Clublocation')

        # Ensure all required fields are present
        if not all([club_name, club_description, sport_name, club_organizer, club_location]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Prepare the document to insert
        new_club = {
            'Clubname': club_name,
            'Clubdescription': club_description,
            'Sportname': sport_name,
            'Cluborganizer': club_organizer,
            'Clublocation': club_location
        }
        
        # Insert the new document into the Clubs collection
        result = clubs_collection.insert_one(new_club)
        
        # Return the id of the new document
        return jsonify({'_id': str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
