from app.models import get_clubs_collection

def get_all_clubs():
    clubs_collection = get_clubs_collection()
    data = list(clubs_collection.find({}))
    for item in data:
        item['_id'] = str(item['_id'])
    return data

def create_club(club_data):
    clubs_collection = get_clubs_collection()
    club_name = club_data.get('Clubname')
    club_description = club_data.get('Clubdescription')
    sport_name = club_data.get('Sportname')
    club_organizer = club_data.get('Cluborganizer')
    club_location = club_data.get('Clublocation')
    if not all([club_name, club_description, sport_name, club_organizer, club_location]):
        raise ValueError('Missing required fields')
    new_club = {
        'Clubname': club_name,
        'Clubdescription': club_description,
        'Sportname': sport_name,
        'Cluborganizer': club_organizer,
        'Clublocation': club_location
    }
    result = clubs_collection.insert_one(new_club)
    return result.inserted_id
