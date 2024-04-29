import imports

def predict_with_ensemble_model(ensemble_model, embeddings):
    predictions = ensemble_model.predict(embeddings)
    return predictions
