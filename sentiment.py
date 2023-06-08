# Install libraries: nltk, flask

import nltk  # Importing the nltk library for natural language processing
from nltk.sentiment.vader import SentimentIntensityAnalyzer  # Importing the SentimentIntensityAnalyzer class from nltk.sentiment.vader


text = "today is a very lucky day"  # The text for sentiment analysis

nltk.download('vader_lexicon')  # Download the lexicon required for sentiment analysis

sid = SentimentIntensityAnalyzer()  # Create an instance of the SentimentIntensityAnalyzer class

score = sid.polarity_scores(str(text))['compound']  # Perform sentiment analysis and extract the compound score

if score > 0:  # Determine if the sentiment is positive
    label = 'The sentiment in the sentence is positive'
elif score == 0:  # Determine if the sentiment is neutral
    label = 'The sentiment in the sentence is neutral'
else:  # The sentiment is negative
    label = 'The sentiment in the sentence is negative'

print(label)  # Print the sentiment label
