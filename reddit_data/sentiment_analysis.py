from flask import Flask
from flask import Blueprint, jsonify, request
from joblib import load
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import tensorflow as tf 
import tensorflow_hub as hub




sentiment_analysis = Blueprint('sentiment_analysis', __name__)


embed_model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

lgb_regressor = load('model/lgb_regressor.pkl')
gb_regressor = load('model/gb_regressor.pkl')
xgb_regressor = load('model/xgb_regressor.pkl')
sgd_regressor = load('model/sdg_regressor.pkl')


# rf_regressor_model = load('model/rf_regressor_model.pkl')
# gb_regressor_model = load('model/gb_regressor_model.pkl')
# xgb_regressor_model = load('model/xgb_regressor_model.pkl')

@sentiment_analysis.route('/sentiment_analysis', methods=['POST'])
def sentiment_regression_endpoint():
    # Get the text data from the request
    data = request.get_json()
    text = data.get('text')

    # Preprocess the text
    text = preprocess_text_sentiment(text)

    if not text.strip():
        # If input text is empty, return scores of 0 for each sentiment category
        sentiment_score = 0
    
    else: 

        embeddings = embed_model([text])

        # Predict sentiment scores using the commented models
        sentiment_score = (
            ( lgb_regressor.predict(embeddings)[0] +
            gb_regressor.predict(embeddings)[0] +
            xgb_regressor.predict(embeddings)[0] +
            sgd_regressor.predict(embeddings)[0] ) / 4
        )   


    return jsonify({'sentiment_score': sentiment_score})


def preprocess_text_sentiment(text):
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+', '', text)

    # Remove emojis
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)

    # Remove special characters and punctuation (excluding spaces)
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenization
    tokens = word_tokenize(text)

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Join tokens
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text
