from ..models.ensemble_model_loader import load_model

sentiment_model = load_model()

def predict_with_ensemble_model(ensemble_model, embeddings):
    predictions = ensemble_model.predict(embeddings)
    return predictions
