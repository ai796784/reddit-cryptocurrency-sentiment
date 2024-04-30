from imports import *


emotion_analysis = Blueprint('emotion_analysis', __name__)


@emotion.route('/emotion_analysis',methods=['POST'])

def emotion_regression_endpoint():
    # Get the text data from the request
    data = request.get_json()
    text = data.get('text')

     text = preprocess_text(text)

    emotion_score = emotion_regression(text)

    return jsonify({'emotion_score': emotion_score})



def preprocess_text(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)
