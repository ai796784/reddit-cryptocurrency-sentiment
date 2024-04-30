sentiment_model = load_model()

def predict_with_ensemble_model(text):
    _,tf-idf_vector = preprocess_text_sentiment(text)
    predictions = sentiment_model.predict(tfidf_vector)
    return predictions
