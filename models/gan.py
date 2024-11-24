import tensorflow as tf
from tensorflow.keras.layers import Dense, LeakyReLU, Dropout
from tensorflow.keras.models import Sequential
import numpy as np

# Generator
def build_generator():
    model = Sequential([
        Dense(128, input_dim=100),
        LeakyReLU(alpha=0.01),
        Dense(256),
        LeakyReLU(alpha=0.01),
        Dense(512),
        LeakyReLU(alpha=0.01),
        Dense(784, activation='tanh')
    ])
    return model

# Discriminator
def build_discriminator():
    model = Sequential([
        Dense(512, input_dim=784),
        LeakyReLU(alpha=0.01),
        Dropout(0.3),
        Dense(256),
        LeakyReLU(alpha=0.01),
        Dropout(0.3),
        Dense(1, activation='sigmoid')
    ])
    return model


def build_gan(generator, discriminator):
    model = Sequential([generator, discriminator])
    return model


def train(generator, discriminator, gan, epochs=10000, batch_size=128):
    
    real_data = np.random.normal(0, 1, (1000, 784))
    for epoch in range(epochs):
        
        noise = np.random.normal(0, 1, (batch_size, 100))
        fake_data = generator.predict(noise)
        X = np.concatenate([real_data[:batch_size], fake_data])
        y = np.concatenate([np.ones((batch_size, 1)), np.zeros((batch_size, 1))])
        d_loss = discriminator.train_on_batch(X, y)

    
        noise = np.random.normal(0, 1, (batch_size, 100))
        y_gen = np.ones((batch_size, 1))
        g_loss = gan.train_on_batch(noise, y_gen)

        if epoch % 100 == 0:
            print(f"Epoch {epoch} | Discriminator Loss: {d_loss:.4f}, Generator Loss: {g_loss:.4f}")

generator = build_generator()
discriminator = build_discriminator()
discriminator.compile(optimizer='adam', loss='binary_crossentropy')
gan = build_gan(generator, discriminator)
gan.compile(optimizer='adam', loss='binary_crossentropy')
train(generator, discriminator, gan)
 
