from flask import Flask, request, Blueprint, send_file
import matplotlib.pyplot as plt
import tempfile
import os
import random


generate_donut_plot = Blueprint('generate_donut_plot', __name__)

TEMP_DIR = "plots"

@generate_donut_plot.route('/generate_donut_plot', methods=['POST'])
def donut_plot_endpoint():
    # Receive the donut plot data from the PHP request
    donut_plot_data = request.json #['donutPlotData']
    
    donut_plot_data = donut_plot_data[0]
    
    # Extract labels and values from the received data
    labels = list(donut_plot_data.keys())
    values = list(donut_plot_data.values())
    
    colors = ['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(len(values))]
    # Generate the donut plot
    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    # plt.title('Donut Plot')
    plt.tight_layout()
    plt.legend(labels, loc="upper left")
    
    # Draw a circle at the center to make it a donut plot
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    

    with tempfile.NamedTemporaryFile(suffix='.png', dir=TEMP_DIR, delete=False) as temp_file:
        temp_file_path = temp_file.name
        plt.savefig(temp_file_path)


    temp_file_path = temp_file.name
    temp_file_name = os.path.basename(temp_file_path)
    
    return temp_file_name  


