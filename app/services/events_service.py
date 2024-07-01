from bson.objectid import ObjectId
from app.models import get_events_collection

def get_all_events():
    events_collection = get_events_collection()
    data = list(events_collection.find({}))
    for item in data:
        item['_id'] = str(item['_id'])
    return data

def create_event(event_data):
    events_collection = get_events_collection()
    event_name = event_data.get('Eventname')
    event_description = event_data.get('Eventdescription')
    sport_name = event_data.get('Sportname')
    event_organizer = event_data.get('Eventorganizer')
    event_cost = event_data.get('Eventcost')
    event_date = event_data.get('Eventdate')
    event_location = event_data.get('Eventlocation')
    if not all([event_name, event_description, sport_name, event_organizer, event_cost, event_date, event_location]):
        raise ValueError('Missing required fields')
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
    return result.inserted_id

def register_for_event(registration_data):
    events_collection = get_events_collection()
    athlete_id = registration_data.get('AthleteId')
    event_id = registration_data.get('EventId')
    if not all([athlete_id, event_id]):
        raise ValueError('Missing required fields')
    event = events_collection.find_one({'_id': ObjectId(event_id)})
    if not event:
        raise ValueError('Event not found')
    return url_for('payments.payment_gateway', athlete_id=athlete_id, event_id=event_id)
