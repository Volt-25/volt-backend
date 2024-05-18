from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, VOLT!'

# MongoDB connection setup
client = MongoClient('mongodb+srv://theplasma:Plasma[][][][][]@theplasma.flv6npg.mongodb.net/?retryWrites=true&w=majority&appName=thePlasma')  # Update with your MongoDB URI if different
db = client['Volt']  # Replace with your database name
collection = db['Events']  # Replace with your collection name

@app.route('/data', methods=['GET'])
def get_all_data():
    try:
        # Fetch all documents from the collection
        data = list(collection.find({}))
        
        # Convert ObjectId to string for JSON serialization
        for item in data:
            item['_id'] = str(item['_id'])
        
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
