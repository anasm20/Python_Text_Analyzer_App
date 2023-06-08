import nltk  # Importing the nltk library for natural language processing
from flask import request, jsonify, Flask, render_template  # Importing necessary modules and classes from Flask
from nltk.sentiment.vader import SentimentIntensityAnalyzer  # Importing the SentimentIntensityAnalyzer class from nltk.sentiment.vader

app = Flask(__name__)  # Creating a Flask application object named 'app'

@app.route('/')  # Route decorator that binds the root URL ('/') to the 'my_form' function
def my_form():
    return render_template('index.html')  # Render the 'index.html' template and return it as the response

@app.route('/', methods=['POST'])  # Route decorator that binds the root URL ('/') with the HTTP method POST to the 'my_form_post' function
def my_form_post():
    text = request.form['text']  # Retrieve the text submitted in the form
    nltk.download('vader_lexicon')  # Download the lexicon required for sentiment analysis
    sid = SentimentIntensityAnalyzer()  # Create an instance of the SentimentIntensityAnalyzer class
    score = sid.polarity_scores(str(text))['compound']  # Perform sentiment analysis and extract the compound score

    if score > 0:  # Determine if the sentiment is positive
        label = 'This sentence is positive 😁'
    elif score == 0:  # Determine if the sentiment is neutral
        label = 'This sentence is neutral 😐'
    else:  # The sentiment is negative
        label = 'This sentence is negative 😕'

    return render_template('index.html', variable=label)  # Render the 'index.html' template and pass the 'label' variable as a parameter

if __name__ == "__main__":
    app.run(port='8088', threaded=False, debug=True)  # Start the Flask development server on port 8088, with debugging mode enabled

