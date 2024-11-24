# utils/helpers.py

import numpy as np

# Example helper function to generate random noise (for GANs)
def generate_noise(batch_size, noise_dim=100):
    return np.random.normal(0, 1, (batch_size, noise_dim))

# Function to save logs to a file
def log_message(message, log_file='logs/app.log'):
    with open(log_file, 'a') as log:
        log.write(f"{message}\n")
