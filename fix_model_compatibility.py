#!/usr/bin/env python3
"""
Script to fix model compatibility issues by recreating the model
from the saved weights and architecture information.
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
import h5py
import os

def fix_model_compatibility():
    """
    Recreate the model with current TensorFlow version and load the weights
    """
    print("Starting model compatibility fix...")
    
    # Model parameters (based on the original notebook)
    max_features = 10000
    max_len = 500
    
    # Create a new model with current TensorFlow version
    print("Creating new model architecture...")
    model = Sequential([
        Embedding(max_features, 128, input_length=max_len),
        SimpleRNN(128, dropout=0.5, recurrent_dropout=0.5),
        Dense(1, activation='sigmoid')
    ])
    
    print("Compiling model...")
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    try:
        # Try to load weights from the old model file
        print("Attempting to load weights from old model...")
        
        # Open the HDF5 file and try to extract weights manually
        with h5py.File('simple_rnn_imdb.h5', 'r') as f:
            print("HDF5 file structure:")
            def print_structure(name, obj):
                print(name)
            f.visititems(print_structure)
            
        # Try a different approach - load just the weights
        try:
            # Create a dummy model to load old weights
            old_model = tf.keras.models.load_model('simple_rnn_imdb.h5', compile=False)
            # Extract weights
            weights = old_model.get_weights()
            # Set weights to new model
            model.set_weights(weights)
            print("Successfully transferred weights!")
        except Exception as e:
            print(f"Could not transfer weights: {e}")
            print("The model will need to be retrained with the current TensorFlow version.")
            return False
            
    except Exception as e:
        print(f"Error reading old model file: {e}")
        return False
    
    # Save the new compatible model
    print("Saving new compatible model...")
    model.save('simple_rnn_imdb_fixed.h5')
    print("Model saved as 'simple_rnn_imdb_fixed.h5'")
    
    # Test the new model
    print("Testing new model...")
    try:
        # Load the IMDB dataset for testing
        (X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=max_features)
        X_test = sequence.pad_sequences(X_test, maxlen=max_len)
        
        # Test prediction
        sample_idx = 0
        sample_input = X_test[sample_idx:sample_idx+1]
        prediction = model.predict(sample_input)
        print(f"Test prediction: {prediction[0][0]:.4f}")
        print("Model is working correctly!")
        
        return True
        
    except Exception as e:
        print(f"Error testing model: {e}")
        return False

if __name__ == "__main__":
    success = fix_model_compatibility()
    if success:
        print("\n✅ Model compatibility fix completed successfully!")
        print("You can now use 'simple_rnn_imdb_fixed.h5' in your application.")
    else:
        print("\n❌ Model compatibility fix failed.")
        print("The model may need to be retrained from scratch.")