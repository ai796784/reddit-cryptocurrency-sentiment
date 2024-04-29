from imports import *

preprocess = Blueprint('preprocess', __name__)

@preprocess.route('/preprocess_text_with_tfidf', methods=['POST'])
def preprocess_text_with_tfidf_endpoint():
    # Get the text data from the request
    data = request.get_json()
    text = data.get('text')

    # Preprocess the text with TF-IDF
    processed_text, tfidf_vector = preprocess_text_with_tfidf(text)

    return jsonify({'processed_text': processed_text, 'tfidf_vector': tfidf_vector.toarray().tolist()})



@preprocess.route('/preprocess', methods=['POST'])
def preprocess_text_endpoint():
    # Get the text data from the request
    data = request.get_json()
    text = data.get('text')

    # Preprocess the text
    processed_text = preprocess_text(text)

    return jsonify({'processed_text': processed_text})



def preprocess_text_with_tfidf(text):
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

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(max_features=3457)
    
    # Fit and transform the text
    tfidf_vector = vectorizer.fit_transform([processed_text])
    return processed_text, tfidf_vector



def preprocess_text(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)
