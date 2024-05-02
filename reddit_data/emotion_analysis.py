from flask import Flask
from flask import Blueprint, request, jsonify
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request

emotion_analysis = Blueprint('emotion_analysis', __name__)


@emotion_analysis.route('/emotion_analysis', methods=['POST'])
def emotion_analysis_endpoint():
    # Get text data from the request
    data = request.get_json()
    text = data.get('text')

    # Task
    task = 'emotion'
    MODEL = f"cardiffnlp/twitter-roberta-base-{task}"

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(MODEL)

    # Download label mapping
    mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
    with urllib.request.urlopen(mapping_link) as f:
        html = f.read().decode('utf-8').split("\n")
        csvreader = csv.reader(html, delimiter='\t')
    labels = [row[1] for row in csvreader if len(row) > 1]

    # Load model
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)

    # Preprocess text
    text = preprocess(text)

    # Encode input
    encoded_input = tokenizer(text, return_tensors='pt')

    # Perform inference
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    # # Rank scores
    # ranking = np.argsort(scores)
    # ranking = ranking[::-1]


    fixed_label_order = ["joy", "sadness", "anger", "optimism"]

    # Prepare response
    for label in fixed_label_order:
        index = labels.index(label) if label in labels else None
        if index is not None:
            score = np.round(float(scores[index]), 4)
            response_data.append({"label": label, "score": score})
        
    # response_data = []
    # for i in range(scores.shape[0]):
    #     label = labels[ranking[i]]
    #     score = np.round(float(scores[ranking[i]]), 4)
    #     response_data.append({"label": label, "score": score})

    return jsonify(response_data)



# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)