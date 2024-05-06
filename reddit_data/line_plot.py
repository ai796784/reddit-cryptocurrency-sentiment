from flask import Flask, request, Blueprint, send_file
import matplotlib.pyplot as plt
import tempfile
import os

generate_line_plot = Blueprint('generate_line_plot', __name__)

TEMP_DIR = "plots"

@generate_line_plot.route('/generate_line_plot', methods=['POST'])
def line_plot_endpoint():
    # Receive the line plot data from the PHP request
    line_plot_data = request.json #['linePlotData']
    # print (line_plot_data)
    
    # Extract x and y values from the received data
    x_values = []
    y_values = []
    for data_point in line_plot_data:
        x_values.append(data_point['num_comments'])
        y_values.append(data_point['interaction'])
    
    # Generate the line plot
    plt.bar(range(len(x_values)), y_values, color='skyblue', alpha=0.7, label='Interaction Rate')
    plt.xlabel('Number of Comments')
    plt.ylabel('Interaction Rate')
    plt.xticks(range(len(x_values)), x_values)
    plt.legend()
    plt.tight_layout()

    # plt.figure(figsize=(8, 6))
    # plt.plot(x_values, y_values, marker='o', linestyle='-')
    # plt.xlabel('Number of Comments')
    # plt.ylabel('Interaction')
    # plt.grid(True)
    # plt.tight_layout()
    

    with tempfile.NamedTemporaryFile(suffix='.png', dir=TEMP_DIR, delete=False) as temp_file:
        temp_file_path = temp_file.name
        plt.savefig(temp_file_path)
    
    temp_file_path = temp_file.name
    temp_file_name = os.path.basename(temp_file_path)
    
    return temp_file_name  

