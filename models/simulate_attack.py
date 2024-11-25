def simulate_multiple_attacks():
    attacks = [
        {"id": 3, "type": "phishing", "status": "trapped"},
        {"id": 4, "type": "malware", "status": "trapped"},
        {"id": 5, "type": "social engineering", "status": "trapped"}
    ]
    for attack in attacks:
        response = requests.post("http://localhost:5000/add_log", json=attack)
        print(response.json())

simulate_multiple_attacks()
