from imports import *

app = Flask(__name__)

# Register blueprints
app.register_blueprint(reddit_data)

if __name__ == '__main__':
    app.run(debug=True)
