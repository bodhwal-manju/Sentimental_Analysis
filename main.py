import numpy as np
import base64
import streamlit as st
import os

# Try to import TensorFlow and load model with error handling
try:
    import tensorflow as tf
    from tensorflow.keras.datasets import imdb
    from tensorflow.keras.preprocessing import sequence 
    from tensorflow.keras.models import load_model
    
    # Load the IMDB word index
    try:
        word_index=imdb.get_word_index()
        reverse_word_index={value:key for key ,value in word_index.items()}
        st.info("✅ Using official IMDB word index")
    except Exception as e:
        # Fallback to simplified word index
        st.warning("Could not download IMDB word index. Using simplified offline version.")
        try:
            import pickle
            with open('simple_word_index.pkl', 'rb') as f:
                word_index = pickle.load(f)
            reverse_word_index = {value: key for key, value in word_index.items()}
            st.info("✅ Using simplified word index")
        except Exception as e2:
            st.error(f"Could not load word index: {e2}")
            word_index = {}
            reverse_word_index = {}
    
    # Try to load the model with compatibility handling
    try:
        # Try to load the fixed model first
        if os.path.exists('simple_rnn_imdb_fixed.h5'):
            model=load_model('simple_rnn_imdb_fixed.h5')
            st.success("✅ Using compatible model version!")
        else:
            model=load_model('simple_rnn_imdb.h5')
        TENSORFLOW_AVAILABLE = True
        MODEL_LOADED = True
    except Exception as model_error:
        st.warning(f"Model loading error: {model_error}")
        st.info("This appears to be a model compatibility issue. The model was trained with an older version of TensorFlow.")
        TENSORFLOW_AVAILABLE = True
        MODEL_LOADED = False
        
except ImportError as e:
    st.error(f"TensorFlow not available: {e}")
    TENSORFLOW_AVAILABLE = False
    MODEL_LOADED = False
except Exception as e:
    st.error(f"Error setting up TensorFlow: {e}")
    TENSORFLOW_AVAILABLE = False
    MODEL_LOADED = False

def decode_review(encoded_review):
    if TENSORFLOW_AVAILABLE:
        return ' '.join([reverse_word_index.get(i - 3,'?') for i in encoded_review])
    else:
        return "TensorFlow not available"

def preprocess_text(text):
    if TENSORFLOW_AVAILABLE:
        words=text.lower().split()
        encoded_review=[word_index.get(word,2)+3 for word in words]
        padded_review=sequence.pad_sequences([encoded_review],maxlen=500)
        return padded_review
    else:
        # Mock preprocessing for demo purposes when TensorFlow is not available
        return [[1] * 500]  # dummy data

##codeee
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Add your background image
add_bg_from_local('pngtree-old-movie-posters-on-the-wall-image_2881318.jpg')



if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'sentiment' not in st.session_state:
    st.session_state.sentiment = ''
if 'prediction' not in st.session_state:
    st.session_state.prediction = 0.0

def close_results():
    st.session_state.show_results = False    



st.markdown("""
<style>
.white-text {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# Use HTML to apply the custom class to your title
st.markdown('<h1 class="white-text">IMDB Movie Review Sentimental Analysis</h1>', unsafe_allow_html=True)

# Rest of your code continues here...
st.markdown('<h4 class="white-text">Enter a Movie Review to classify it as positive or Negative</h4>', unsafe_allow_html=True)
user_input=st.text_area('Enter your movie review here:', placeholder="Type your movie review here...")

if st.button('Classify'):
    if user_input.strip():
        if TENSORFLOW_AVAILABLE and MODEL_LOADED:
            preprocessed_input=preprocess_text(user_input)
            prediction=model.predict(preprocessed_input)
            sentiment='Positive' if prediction[0][0]>0.5 else 'Negative'
            prediction_score = prediction[0][0]
        elif TENSORFLOW_AVAILABLE:
            # TensorFlow is available but model failed to load
            st.error("Model could not be loaded due to compatibility issues. This may be due to version differences.")
            # Mock prediction for demo
            import random
            prediction_score = random.random()
            sentiment = 'Positive' if prediction_score > 0.5 else 'Negative'
            st.warning("Showing demo prediction instead of actual model prediction.")
        else:
            # Mock prediction when TensorFlow is not available
            st.warning("TensorFlow is not available. Showing demo functionality.")
            import random
            prediction_score = random.random()  # Random prediction between 0 and 1
            sentiment = 'Positive' if prediction_score > 0.5 else 'Negative'

        st.session_state.show_results = True
        st.session_state.sentiment = sentiment
        st.session_state.prediction = prediction_score
    else:
        st.error("Please enter a movie review before classifying!")

# Display results if available
if st.session_state.show_results:
    # Determine box color based on sentiment
    box_color = "#28a745" if st.session_state.sentiment == 'Positive' else "#dc3545"

    # Create a styled pop-up box with a functional close button
    st.markdown(f"""
    <style>
    .result-box {{
        background-color: {box_color};
        color: white;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        position: relative;
    }}
    .close-button {{
        position: absolute;
        top: 10px;
        right: 10px;
        background-color: transparent;
        border: none;
        color: white;
        font-size: 20px;
        cursor: pointer;
    }}
    </style>
    
    <div class="result-box" id="result-box">
        <button class="close-button" onclick="closeResults()">✖</button>
        <h3>Analysis Results:</h3>
        <p><strong>Sentiment:</strong> {st.session_state.sentiment}</p>
        <p><strong>Prediction Score:</strong> {st.session_state.prediction:.4f}</p>
    </div>

    <script>
    function closeResults() {{
        document.getElementById('result-box').style.display = 'none';
        window.parent.postMessage({{
            type: 'streamlit:setComponentValue',
            value: false
        }}, '*');
    }}
    </script>
    """, unsafe_allow_html=True)
    
    if st.button('Close Results', key='close-results', on_click=close_results):
        pass    

    st.balloons()
    

