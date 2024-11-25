# reinforcement.py
from collections import deque
import random

class DecoyDeploymentAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.9):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_table = {}

    def get_action(self, state):
        if state not in self.q_table:
            self.q_table[state] = [0, 0]
        return random.choice([0, 1])  # 0 = no decoy, 1 = deploy decoy

    def update_q_value(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = [0, 0]
        if next_state not in self.q_table:
            self.q_table[next_state] = [0, 0]
        
        best_next_action = max(self.q_table[next_state])
        self.q_table[state][action] = self.q_table[state][action] + self.learning_rate * (reward + self.discount_factor * best_next_action - self.q_table[state][action])

# In your optimize_decoy_deployment function
active_traps_count = 0  # Track the number of active traps

def optimize_decoy_deployment(anomaly_detected=False):
    global active_traps_count
    
    # Base trap deployment decision, could depend on external factors (e.g., data traffic, attack patterns)
    if anomaly_detected:
        active_traps_count += 1  # Add a new trap when an anomaly is detected
    else:
        active_traps_count = max(0, active_traps_count - 1)  # Decrease traps if no anomalies
    
    return active_traps_count



class TrapDeploymentRL:
    def __init__(self):
        self.state = 0  # Initial state, could represent system health or risk level
        self.action_space = [0, 1]  # 0: Do nothing, 1: Deploy a trap
        self.reward_queue = deque(maxlen=10)
    
    def choose_action(self):
        # Choose action based on the current state (simplified for now)
        if self.state > 5:  # Example threshold for when to deploy a trap
            return 1  # Deploy trap
        else:
            return 0  # Do nothing
    
    def update_state(self, anomaly_detected):
        if anomaly_detected:
            self.state += 1  # Increase state if anomaly detected
        else:
            self.state -= 1  # Decrease state if no anomaly
    
    def get_reward(self, action):
        # Reward could be based on the success of the action (e.g., whether it blocked an attack)
        return 1 if action == 1 else 0
    
    def train(self):
        # RL training logic (could involve Q-learning or other methods)
        action = self.choose_action()
        reward = self.get_reward(action)
        self.reward_queue.append(reward)
        # Update strategy based on past actions and rewards (this is a simplified example)
