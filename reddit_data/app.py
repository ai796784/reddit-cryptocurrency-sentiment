from flask import Flask
from flask import Blueprint, jsonify, request
from reddit_data import reddit_data

app = Flask(__name__)

# Register blueprints
app.register_blueprint(reddit_data)

if __name__ == '__main__':
    app.run(debug=True)
