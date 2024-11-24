# data/dataset_preparation.py

import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(file_path='data/sample_data.csv'):
    # Load dataset
    data = pd.read_csv(file_path)

    # Convert categorical variables (attack_type, system_status) into numerical values
    data['attack_type'] = data['attack_type'].astype('category').cat.codes
    data['system_status'] = data['system_status'].astype('category').cat.codes

    # Example: Preprocessing (Standardization for numeric data)
    scaler = StandardScaler()
    features = data[['attack_type', 'source_ip']]  # Only numeric columns for scaling
    features_scaled = scaler.fit_transform(features)

    # You can choose to return the full dataset or only the relevant features
    return features_scaled, data['detected'].values
