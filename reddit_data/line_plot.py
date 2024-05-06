from flask import Flask, request, Blueprint, send_file
import matplotlib.pyplot as plt
import tempfile
import os
import numpy as np

generate_line_plot = Blueprint('generate_line_plot', __name__)

TEMP_DIR = "plots"

@generate_line_plot.route('/generate_line_plot', methods=['POST'])
def line_plot_endpoint():
    # Receive the line plot data from the PHP request
    line_plot_data = request.json #['linePlotData']
    # print (line_plot_data)
    
    # Extract x and y values from the received data
    x_values = []
    y_num_comments = []
    y_interaction = []
    for data_point in line_plot_data:
        # x_values.append(data_point['x_value'])
        y_num_comments.append(data_point['num_comments'])
        y_interaction.append(data_point['interaction'])

    
    # Generate the grouped bar plot
    fig, ax = plt.figure(figsize=(8, 6))
    bar_width = 0.2
    index = np.arange(len(x_values))
    # plt.title('Bar Plot')
    rects1 = ax.bar(index, y_num_comments, bar_width, color="blue", label='Number of Comments')
    rects2 = ax.bar(index + bar_width, y_interaction, bar_width, color="red", label='Interaction')

    ax.legend()
    # plt.grid(True)
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

