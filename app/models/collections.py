from flask import current_app

def get_events_collection():
    return current_app.db['Events']

def get_clubs_collection():
    return current_app.db['Clubs']
