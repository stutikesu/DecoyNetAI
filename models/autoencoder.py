import torch
import torch.nn as nn

class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(5, 1024),  # Adjusted input size to 5
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 1024),
            nn.ReLU(),
            nn.Linear(1024, 5),  # Adjusted output size to 5
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x
    

def detect_anomaly(input_data):
    # Convert input data (which is a list) to a PyTorch tensor
    input_data_tensor = torch.tensor(input_data, dtype=torch.float32)
    
    # Ensure the input has the appropriate shape for the model
    input_data_tensor = input_data_tensor.unsqueeze(0)  # Adds a batch dimension (shape: [1, N])
    
    # Instantiate the Autoencoder model
    autoencoder = Autoencoder()
    
    # Pass the tensor through the autoencoder model
    output = autoencoder(input_data_tensor)
    
    # Compute the reconstruction error or any other anomaly detection logic here
    reconstruction_error = torch.mean((input_data_tensor - output) ** 2)
    
    # Define a threshold for anomaly detection
    anomaly_threshold = 0.05  # Example threshold; adjust as needed
    
    # Check if the reconstruction error exceeds the threshold
    anomaly_detected = reconstruction_error > anomaly_threshold
    
    return anomaly_detected
