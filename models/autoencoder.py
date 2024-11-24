 
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
import numpy as np

# Autoencoder
input_dim = 30  # Example feature dimension
input_layer = Input(shape=(input_dim,))
encoded = Dense(14, activation='relu')(input_layer)
encoded = Dense(7, activation='relu')(encoded)
decoded = Dense(14, activation='relu')(encoded)
decoded = Dense(input_dim, activation='sigmoid')(decoded)

autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Generate synthetic data
data = np.random.random((1000, input_dim))
autoencoder.fit(data, data, epochs=50, batch_size=32)

# Detect anomalies
reconstructions = autoencoder.predict(data)
mse = np.mean(np.power(data - reconstructions, 2), axis=1)
threshold = np.percentile(mse, 95) 
anomalies = mse > threshold
print("Detected anomalies:", anomalies)
