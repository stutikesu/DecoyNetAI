 
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy attacker logs
logs = [{"id": 1, "type": "phishing", "status": "trapped"}]

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs)

@app.route('/add_log', methods=['POST'])
def add_log():
    new_log = request.json
    logs.append(new_log)
    return jsonify({"message": "Log added"}), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)
