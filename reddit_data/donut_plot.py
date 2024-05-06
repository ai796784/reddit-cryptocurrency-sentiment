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

    nonzero_labels = [label for label, value in donut_plot_data.items() if value != 0]
    nonzero_values = [value for value in donut_plot_data.values() if value != 0]
    
    
    colors = ['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(len(nonzero_values))]
    explode = [0.05 if i == max(nonzero_values) else 0 for i in nonzero_values]
    
    plt.figure(figsize=(10, 8))
    plt.pie(nonzero_values, labels=nonzero_labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode)
    plt.legend(nonzero_labels, loc="upper left", bbox_to_anchor=(1, 0.7))  
    plt.axis('equal')  
    
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    

    with tempfile.NamedTemporaryFile(suffix='.png', dir=TEMP_DIR, delete=False) as temp_file:
        temp_file_path = temp_file.name
        plt.savefig(temp_file_path)


    temp_file_path = temp_file.name
    temp_file_name = os.path.basename(temp_file_path)
    
    return temp_file_name  


