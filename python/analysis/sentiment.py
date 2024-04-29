sentiment_model = load_model()

def predict_with_ensemble_model(text):
    preprocessed_text,tf-idf_vector = preprocess_text_with_tfidf(text)
    predictions = sentiment_model.predict(tfidf_vector)
    result = {
        "preprocessed_text": preprocessed_text,
        "sentiment_score": sentiment_score
    }
    
    return result
