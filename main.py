from flask import Flask, render_template, jsonify, request
from models.gan import generate_decoy  # GAN for generating decoys
from models.autoencoder import detect_anomaly  # Autoencoder for anomaly detection
from models.reinforcement import TrapDeploymentRL  # Reinforcement learning for trap optimization
from utils.helpers import log_message, format_decoy_data, load_state, save_state  # Helper functions
from utils.config import LOGGING_ENABLED, ANOMALY_DETECTION_THRESHOLD  # Configurations

app = Flask(__name__)

# Initialize the RL agent for trap deployment
trap_rl_agent = TrapDeploymentRL()

# Global variable to keep track of the active traps
def get_active_traps_count():
    state = load_state()
    return state.get("active_traps", 0)

def update_active_traps_count(count):
    state = load_state()
    state["active_traps"] = count
    save_state(state)

@app.route('/')
def dashboard():
    # Example flow:
    state = load_state()
    return render_template('dashboard.html', 
                           active_traps=state['active_traps'], 
                           decoy_status=state["decoy_status"], 
                           state=state)

@app.route('/deploy-decoy', methods=['POST'])
def deploy_decoy():
    """Route to deploy a new decoy."""
    # Generate a new decoy (or update based on anomaly)
    decoy = generate_decoy()  # Assume it generates a new decoy for deployment
    formatted_decoy = format_decoy_data({"id": 1, "type": "file", "status": "active"})
    
    # Log the decoy deployment if logging is enabled
    if formatted_decoy and LOGGING_ENABLED:
        log_message(f"Decoy deployed: {formatted_decoy}")
    
    # Update state with new active traps
    new_count = get_active_traps_count() + 1
    update_active_traps_count(new_count)
    
    # Update decoy status
    state = load_state()
    state["decoy_status"] = "active"
    save_state(state)
    
    return jsonify({
        'active_traps': new_count,
        'decoy_status': state["decoy_status"]
    })

@app.route('/get-dashboard-data')
def get_dashboard_data():
    """Return the latest data as JSON for real-time updates."""
    state = load_state()
    decoy_status = state.get("decoy_status", "inactive")
    return jsonify({
        'active_traps': state["active_traps"],
        'decoy_status': decoy_status
    })

if __name__ == '__main__':
    app.run(debug=True)
