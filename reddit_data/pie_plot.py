from flask import Flask, request, Blueprint, send_file
import matplotlib.pyplot as plt
import tempfile
import os

generate_pie_plot = Blueprint('generate_pie_plot', __name__)

TEMP_DIR = 'plots'


@generate_pie_plot.route('/generate_pie_plot', methods=['POST'])
def pie_plot_endpoint():
    # Receive the pie plot data from the PHP request
    pie_plot_data = request.json #['piePlotData']

    pie_plot_data = pie_plot_data[0]

    # Extract labels and values from the received data
    labels = list(pie_plot_data.keys())
    values = list(pie_plot_data.values())
    
    nonzero_labels = [label for label, value in zip(labels, values) if value != 0]
    nonzero_values = [value for value in values if value != 0]
    
    plt.figure(figsize=(8, 6))
    patches, texts, autotexts = plt.pie(nonzero_values, labels=nonzero_labels, autopct='%1.1f%%', startangle=90, labeldistance=1.15)
    plt.legend(patches, nonzero_labels, loc="upper left")

    plt.tight_layout()
    
    for autotext in autotexts:
        autotext.set_color('white')  
        autotext.set_fontsize(10)  

    with tempfile.NamedTemporaryFile(suffix='.png', dir=TEMP_DIR, delete=False) as temp_file:
        temp_file_path = temp_file.name
        plt.savefig(temp_file_path)
    

    temp_file_path = temp_file.name
    temp_file_name = os.path.basename(temp_file_path)
    
    return temp_file_name  

    

