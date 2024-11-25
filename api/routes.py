


from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy attacker logs
logs = [{"id": 1, "type": "phishing", "status": "trapped"}]

@app.route('/add_log', methods=['POST'])
def add_log():
    new_log = request.json  # Expecting JSON data from the request
    if not new_log:
        return jsonify({"error": "No data provided"}), 400
    logs.append(new_log)
    return jsonify({"message": "Log added"}), 201

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)
