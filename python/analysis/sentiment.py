sentiment_model = load_model()

def predict_with_ensemble_model(tfidf_vector):
    predictions = sentiment_model.predict(tfidf_vector)
    return sentiment_score
