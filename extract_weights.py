#!/usr/bin/env python3
"""
Script to manually extract weights and create a compatible model
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
import h5py

def extract_weights_and_create_model():
    """
    Manually extract weights from the old model and create a new compatible one
    """
    print("Extracting weights manually from the old model...")
    
    # Parameters
    max_features = 10000
    max_len = 500
    
    try:
        # Extract weights manually from HDF5 file
        with h5py.File('simple_rnn_imdb.h5', 'r') as f:
            # Extract embedding weights
            embedding_weights = f['model_weights/embedding/embedding/embeddings:0'][()]
            print(f"Embedding weights shape: {embedding_weights.shape}")
            
            # Extract SimpleRNN weights
            rnn_kernel = f['model_weights/simple_rnn/simple_rnn/simple_rnn_cell/kernel:0'][()]
            rnn_recurrent_kernel = f['model_weights/simple_rnn/simple_rnn/simple_rnn_cell/recurrent_kernel:0'][()]
            rnn_bias = f['model_weights/simple_rnn/simple_rnn/simple_rnn_cell/bias:0'][()]
            
            print(f"RNN kernel shape: {rnn_kernel.shape}")
            print(f"RNN recurrent kernel shape: {rnn_recurrent_kernel.shape}")
            print(f"RNN bias shape: {rnn_bias.shape}")
            
            # Extract Dense layer weights
            dense_kernel = f['model_weights/dense/dense/kernel:0'][()]
            dense_bias = f['model_weights/dense/dense/bias:0'][()]
            
            print(f"Dense kernel shape: {dense_kernel.shape}")
            print(f"Dense bias shape: {dense_bias.shape}")
        
        # Create new model with current TensorFlow
        print("Creating new compatible model...")
        model = Sequential([
            Embedding(max_features, 128),
            SimpleRNN(128, dropout=0.5, recurrent_dropout=0.5),
            Dense(1, activation='sigmoid')
        ])
        
        # Build the model by calling it with dummy data
        dummy_input = np.zeros((1, max_len))
        _ = model(dummy_input)
        
        # Set the extracted weights
        print("Setting weights...")
        model.layers[0].set_weights([embedding_weights])  # Embedding layer
        model.layers[1].set_weights([rnn_kernel, rnn_recurrent_kernel, rnn_bias])  # SimpleRNN layer
        model.layers[2].set_weights([dense_kernel, dense_bias])  # Dense layer
        
        # Compile the model
        model.compile(
            optimizer='adam',
            loss='binary_crossentropy',
            metrics=['accuracy']
        )
        
        # Save the new model
        model.save('simple_rnn_imdb_fixed.h5')
        print("New compatible model saved as 'simple_rnn_imdb_fixed.h5'")
        
        # Test the model
        print("Testing the new model...")
        # Load test data
        (_, _), (X_test, y_test) = imdb.load_data(num_words=max_features)
        X_test = sequence.pad_sequences(X_test, maxlen=max_len)
        
        # Test prediction
        sample_prediction = model.predict(X_test[0:1])
        print(f"Test prediction: {sample_prediction[0][0]:.4f}")
        
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    success = extract_weights_and_create_model()
    if success:
        print("\n✅ Successfully created compatible model!")
    else:
        print("\n❌ Failed to create compatible model.")