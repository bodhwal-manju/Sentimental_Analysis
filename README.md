<h1 align="center" id="title">IMDB Movie Review(Sentimental Analysis)</h1>
<h2>🤜Overview</h2>
This project is a web application that performs sentiment analysis on IMDB movie reviews. It uses a Simple Recurrent Neural Network (RNN) to classify user-input movie reviews as either positive or negative.


<h2>Features</h2>
    <ul>
        <li><strong>Web Interface:</strong> A user-friendly web application built with Streamlit, featuring a clean design with a movie-themed background.</li>
        <li><strong>Real-time Analysis:</strong> Users can input their movie reviews into a text area and get instant sentiment classification.</li>
        <li><strong>Sentiment Classification:</strong> The app classifies reviews as either "Positive" or "Negative" based on the input text.</li>
        <li><strong>Visual Feedback:</strong> The application uses colorful floating balloons to create an engaging and interactive user experience. </li>
         <li><strong>Analysis Results Display:</strong>The sentiment and potentially a confidence score are displayed in a green or red box at the bottom of the interface depending on the score..
    </ul>
<h2>Project Screenshots:</h2>

<img src='https://github.com/bodhwal-manju/Sentimental_Analysis/blob/main/project_photo/Screenshot%202024-08-27%20161409.png'/>
<img src="https://github.com/bodhwal-manju/Sentimental_Analysis/blob/main/project_photo/Screenshot%202024-08-27%20161433.png"/>
<img src="https://github.com/bodhwal-manju/Sentimental_Analysis/blob/main/project_photo/Screenshot%202024-08-27%20161540.png"/>
<img src="https://github.com/bodhwal-manju/Sentimental_Analysis/blob/main/project_photo/Screenshot%202024-08-27%20161643.png"/>

<h2>🚀 Demo</h2>

[https://drive.google.com/file/d/1pUieaDNDAqpWPLZwE7xhyflvdTC3HWIa/view?usp=drive_link](https://drive.google.com/file/d/1pUieaDNDAqpWPLZwE7xhyflvdTC3HWIa/view?usp=drive_link)

<h2>Technical Aspects</h2>
    <ul>
        <li><strong>Backend:</strong>Utilizes a Simple RNN model trained on IMDB movie review data.</li>
        <li><strong>Frontend:</strong> Built using Streamlit, a Python library for creating web applications.</li>
        <li><strong>Machine Learning:</strong> Implements natural language processing (NLP) techniques for text classification.</li>
    </ul>
<h2>🛠️ Installation Steps:</h2>

<p>1. Clone this repository</p>

```
https://github.com/bodhwal-manju/VidNotes_AI.git
```

<p>2. Navigate to the project directory:</p>

```
cd Sentimental_Analysis
```

<p>3. Create Virtual Environment(Using venv (Python 3 built-in module))</p>

```
python -m venv venv
```

<p>4. Activate the virtual environment(On Windows):</p>

```
venv\Scripts\activate
```

<p>5. Install Requirements</p>

```
pip install -r requirements.txt
```
<h2>Usage</h2>
    <ol>
        <li><strong>Run the Streamlit application:</strong>
            <pre><code>streamlit run app.py</code></pre>
        </li>
        <li><strong>Input Review:</strong>
            <p>Open your web browser and navigate to the provided local URL. Enter the Review.</p>
        </li>
        <li><strong>Result:</strong>
            <p>Click on the "Classify" button to get the classification Result. Use the "close Results" button to re-enter the new review</p>
        </li>
    </ol>


   
<h2>🛡️ License:</h2>

This project is licensed under the MIT License
