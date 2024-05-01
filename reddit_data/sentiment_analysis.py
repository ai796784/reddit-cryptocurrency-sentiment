from joblib import load
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer



sentiment_analysis = Blueprint('sentiment_analysis', __name__)

@sentiment.route('/sentiment_analysis', methods=['POST'])
def sentiment_regression_endpoint():
    # Get the text data from the request
    data = request.get_json()
    text = data.get('text')

    # Preprocess the text
    text = preprocess_text_sentiment(text)

    # Calculate sentiment score
    sentiment_score = sentiment_regression(text)

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

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Join tokens
    processed_text = ' '.join(tokens)
    return processed_text

def sentiment_regression(text):
    vectorizer = TfidfVectorizer(max_features=3457)
    tfidf_vector = vectorizer.fit_transform([text])

    # Load regressor models
    rf_regressor_model = load('/model/rf_regressor_model.pkl')
    gb_regressor_model = load('/model/gb_regressor_model.pkl')
    xgb_regressor_model = load('/model/xgb_regressor_model.pkl')

    # Predict sentiment scores
    sentiment_score = (
        rf_regressor_model.predict(tfidf_vector)[0] +
        gb_regressor_model.predict(tfidf_vector)[0] +
        xgb_regressor_model.predict(tfidf_vector)[0]
    )

    return sentiment_score
