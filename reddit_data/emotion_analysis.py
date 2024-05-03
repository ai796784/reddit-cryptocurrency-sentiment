from flask import Flask
from flask import Blueprint, request, jsonify
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request

emotion_analysis = Blueprint('emotion_analysis', __name__)

# Task
task = 'emotion'    
MODEL = f"cardiffnlp/twitter-roberta-base-{task}"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL)

max_seq_length = 514
tokenizer.model_max_length = max_seq_length

# Download label mapping
mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
with urllib.request.urlopen(mapping_link) as f:
    html = f.read().decode('utf-8').split("\n")
    csvreader = csv.reader(html, delimiter='\t')
    labels = [row[1] for row in csvreader if len(row) > 1]

# Load model
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

@emotion_analysis.route('/emotion_analysis', methods=['POST'])
def emotion_analysis_endpoint():

    fixed_label_order = ["joy", "sadness", "anger", "optimism"]
    response_data = []
    
    
    # Get text data from the request
    data = request.get_json()
    text = data.get('text')

    # Preprocess text
    text = preprocess(text)

    if not text.strip():
        # If input text is empty, return scores of 0 for each sentiment category
        response_data = [{"label": label, "score": 0.0} for label in fixed_label_order]
    else:
        encoded_input = tokenizer(text, return_tensors='pt')
        output = model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        for label in fixed_label_order:
            index = labels.index(label) if label in labels else None
            if index is not None:
                score = np.round(float(scores[index]), 4)
                response_data.append({"label": label, "score": score})

    return jsonify(response_data)



# Preprocess text (username and link placeholders)
# def preprocess(text):
#     new_text = []
#     for t in text.split(" "):
#         t = '@user' if t.startswith('@') and len(t) > 1 else t
#         t = 'http' if t.startswith('http') else t
#         new_text.append(t)
#     return " ".join(new_text)

# def preprocess(text):
#     new_text = []
#     lines = text.split("\n")
    
#     for line in lines:
#         # Skip lines that are unlikely to contain sentiment-bearing content
#         if line.startswith(("**", "#", ">>>", "●", ">", "-", "*", ">", "&")):
#             continue
        
#         words = line.split(" ")
#         processed_words = []
#         for word in words:
#             # Preprocess words
#             word = '@user' if word.startswith('@') and len(word) > 1 else word
#             word = 'http' if word.startswith('http') else word
#             processed_words.append(word)
#         processed_line = " ".join(processed_words)
#         new_text.append(processed_line)
    
#     return "\n".join(new_text)


def preprocess(text, max_length=100):
    new_text = []
    lines = text.split("\n")
    
    for line in lines:
        # Skip lines that are unlikely to contain sentiment-bearing content
        if line.startswith(("**", "#", ">>>", "●", ">", "-", "*", ">", "&")):
            continue
        
        words = line.split(" ")
        processed_words = []
        line_length = 0
        for word in words:
            # Preprocess words
            word = '@user' if word.startswith('@') and len(word) > 1 else word
            word = 'http' if word.startswith('http') else word
            if line_length + len(word) + 1 <= max_length:  # Check if adding word exceeds max_length
                processed_words.append(word)
                line_length += len(word) + 1  # Add 1 for space
            else:
                break  # Stop adding words if max_length is exceeded
        processed_line = " ".join(processed_words)
        new_text.append(processed_line)
    
    return "\n".join(new_text)
