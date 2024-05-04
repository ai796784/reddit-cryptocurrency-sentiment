from flask import Flask, request, Blueprint, send_file
from reddit_data import reddit_data
from sentiment_analysis import sentiment_analysis
from emotion_analysis import emotion_analysis
from line_plot import generate_line_plot
from pie_plot import generate_pie_plot
from donut_plot import generate_donut_plot
from heat_plot import generate_heat_plot
from radar_plot import generate_radar_plot

app = Flask(__name__)

# Register blueprints
app.register_blueprint(reddit_data)
app.register_blueprint(sentiment_analysis)
app.register_blueprint(emotion_analysis)
app.register_blueprint(generate_line_plot)
app.register_blueprint(generate_pie_plot)
app.register_blueprint(generate_donut_plot)
app.register_blueprint(generate_heat_plot)
app.register_blueprint(generate_radar_plot)

if __name__ == '__main__':
    app.run(debug=True)
