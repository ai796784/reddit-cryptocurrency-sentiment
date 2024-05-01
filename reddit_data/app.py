from flask import Flask
from flask import Blueprint, jsonify, request
from reddit_data import reddit_data
from sentiment_analysis import sentiment_analysis
from emotion_analysis import emotion_analysis

app = Flask(__name__)

# Register blueprints
app.register_blueprint(reddit_data)
app.register_blueprint(sentiment_analysis)
app.register_blueprint(emotion_analysis)


if __name__ == '__main__':
    app.run(debug=True)
