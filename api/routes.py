# api/routes.py

from flask import Blueprint, jsonify, request
from utils.helpers import log_message
from models.gan import train

# Create a Blueprint for routing
bp = Blueprint('api', __name__)

# Route to get logs
@bp.route('/logs', methods=['GET'])
def get_logs():
    try:
        with open('logs/app.log', 'r') as file:
            logs = file.readlines()
        return jsonify(logs)
    except FileNotFoundError:
        return jsonify({"error": "Logs not found"}), 404

# Route to add a new log entry
@bp.route('/add_log', methods=['POST'])
def add_log():
    new_log = request.json
    log_message(str(new_log))  # Store log to app.log
    return jsonify({"message": "Log added"}), 201

# Route to start GAN training (example)
@bp.route('/train_gan', methods=['POST'])
def train_gan():
    train()
    return jsonify({"message": "GAN training started"}), 200
 
