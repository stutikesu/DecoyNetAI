import requests

def simulate_attack():
    payload = {"id": 2, "type": "network", "status": "trapped"}
    try:
        response = requests.post("http://127.0.0.1:5000/add_log", json=payload)
        print(f"Payload sent: {payload}")
        print(f"Response: {response.text}")

        # Check if the response is valid (i.e., contains a success message)
        if response.status_code == 201:
            return "Real-Time Cyber Deception: Successfully diverted an attack attempt using dynamic decoys, reducing the likelihood of a successful breach."
        else:
            return "Real-Time Cyber Deception: No new decoy data added."
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return f"Request Error: {e}"
