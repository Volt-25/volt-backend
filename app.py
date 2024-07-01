from flask import Flask, request, jsonify, redirect, url_for
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

@app.route('/api/events', methods=['GET'])
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

@app.route('/api/events', methods=['POST'])
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
@app.route('/api/clubs', methods=['GET'])
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
@app.route('/api/clubs', methods=['POST'])
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
    

@app.route('/api/events/register', methods=['POST'])
def register_for_event():
    try:
        # Extract data from request
        registration_data = request.get_json()
        
        # Validate and extract individual fields
        athlete_id = registration_data.get('AthleteId')
        event_id = registration_data.get('EventId')

        # Ensure all required fields are present
        if not all([athlete_id, event_id]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Check if the event exists
        event = events_collection.find_one({'_id': ObjectId(event_id)})
        if not event:
            return jsonify({'error': 'Event not found'}), 404
        
        # Here you can add logic to calculate payment amount or any other necessary data
        
        # Redirect the athlete to the payment gateway
        return redirect(url_for('payment_gateway', athlete_id=athlete_id, event_id=event_id))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/payment_gateway', methods=['GET'])
def payment_gateway():
    try:
        # Extract athlete ID and event ID from request arguments
        athlete_id = request.args.get('athlete_id')
        event_id = request.args.get('event_id')

        # Here you can add logic to fetch athlete and event details for displaying on the payment gateway page
        
        # Redirect the athlete to the payment gateway page
        # For demonstration purposes, let's assume the payment gateway URL is '/payment'
        return redirect(url_for('payment'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/payment', methods=['GET'])
def payment():
    try:
        # Here you can render the payment page or redirect to the actual payment gateway URL
        # For demonstration purposes, let's just return a message
        return 'This is the payment page. Implement your payment logic here.'
    except Exception as e:
        return jsonify({'error': str(e)}), 500



# if __name__ == '__main__':
#     app.run(debug=True)