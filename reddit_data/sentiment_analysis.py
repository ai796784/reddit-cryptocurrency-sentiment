from flask import Flask
from flask import Blueprint, jsonify, request
from joblib import load
import numpy as np
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer



sentiment_analysis = Blueprint('sentiment_analysis', __name__)

rf_regressor_model = load('model/rf_regressor_model.pkl')
gb_regressor_model = load('model/gb_regressor_model.pkl')
xgb_regressor_model = load('model/xgb_regressor_model.pkl')

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
        vectorizer = TfidfVectorizer(max_features=3457)
        tfidf_vector = vectorizer.fit_transform([text])
        if tfidf_vector.shape[1] < 3457:
            num_missing_features = 3457 - tfidf_vector.shape[1]
            tfidf_vector = np.pad(tfidf_vector.toarray(), ((0, 0), (0, num_missing_features)), mode='constant', constant_values=0.0)
            sentiment_score = (
                rf_regressor_model.predict(tfidf_vector)[0] +
                gb_regressor_model.predict(tfidf_vector)[0] +
                xgb_regressor_model.predict(tfidf_vector)[0]
            )

    return jsonify({'sentiment_score': sentiment_score})

# custom_words = [
#     "Bitcoin", "Ethereum", "Ripple", "Litecoin", "Dogecoin", "Blockchain",
#     "Altcoin", "Wallet", "Hodl", "Mining", "Exchange", "Decentralized",
#     "Token", "Smart contract", "DeFi", "Subreddit", "Karma", "Upvote",
#     "Downvote", "Mod", "Cake day", "Frontpage", "Gold", "Silver", "Platinum",
#     "Redditor", "Snoo", "Cake icon", "IAMA", "ELI5"
# ]


def preprocess_text_sentiment(text, max_length=200):
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

    # Truncate tokens to fit max_length
    truncated_tokens = []
    token_length = 0
    for token in tokens:
        if token_length + len(token) + 1 <= max_length:  # Check if adding token exceeds max_length
            truncated_tokens.append(token)
            token_length += len(token) + 1  # Add 1 for space
        else:
            break  # Stop adding tokens if max_length is exceeded

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in truncated_tokens]

    # Join tokens
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text