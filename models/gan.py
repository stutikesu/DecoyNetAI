import torch
import torch.nn as nn
import torch.optim as optim
from models.autoencoder import Autoencoder
from utils.helpers import log_message
from utils.config import ANOMALY_DETECTION_THRESHOLD, GAN_NOISE_DIM

class GAN:
    def __init__(self):
        """Initializes GAN model and loads pre-trained autoencoder weights."""
        self.autoencoder = Autoencoder()
        try:
            self.autoencoder.load_state_dict(torch.load('autoencoder_model.pth'))
            self.autoencoder.eval()
        except FileNotFoundError:
            log_message("Error: Autoencoder model not found!")
        
        self.noise_dim = GAN_NOISE_DIM
        self.generator = self._build_generator()
        self.discriminator = self._build_discriminator()

    def _build_generator(self):
        """Builds the generator part of the GAN."""
        generator = nn.Sequential(
            nn.Linear(self.noise_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, 1024),
            nn.ReLU(),
            nn.Linear(1024, 2048),
            nn.Tanh()
        )
        return generator

    def _build_discriminator(self):
        """Builds the discriminator part of the GAN."""
        discriminator = nn.Sequential(
            nn.Linear(2048, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )
        return discriminator

    def generate_decoy(self):
        """Generates a decoy using the GAN generator."""
        noise = torch.randn(1, self.noise_dim)
        decoy = self.generator(noise)
        decoy = decoy.detach().numpy()
        return decoy

def generate_decoy():
    gan = GAN()  # Instantiate the GAN class
    return gan.generate_decoy()  # Generate a decoy from the GAN instance

# Example of using the generate_decoy function
if __name__ == "__main__":
    decoy = generate_decoy()
    print(f"Generated Decoy: {decoy}")
