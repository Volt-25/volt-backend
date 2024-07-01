from flask import Flask
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object('config.Config')

    # MongoDB connection setup
    client = MongoClient(app.config['MONGO_URI'])
    app.db = client[app.config['MONGO_DB_NAME']]

    # Register Blueprints
    from app.views import events, clubs, payments
    app.register_blueprint(events.bp)
    app.register_blueprint(clubs.bp)
    app.register_blueprint(payments.bp)

    return app
