from flask import Flask, request, jsonify
from flask_cors import CORS
from models import participants

app = Flask(__name__)
CORS(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    data['isHackathon'] = 'Hackathon' in data.get('events', [])
    participants.insert_one(data)
    return jsonify({"message": "Registered successfully"}), 201

@app.route('/participants', methods=['GET'])
def get_participants():
    all_participants = list(participants.find({}, {'_id': 0}))
    return jsonify(all_participants)

if __name__ == '__main__':
    app.run(debug=True)
