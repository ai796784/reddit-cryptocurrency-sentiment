from flask import Flask, request, Blueprint, send_file
import matplotlib.pyplot as plt
import tempfile

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
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, marker='o', linestyle='-')
    plt.title('Line Plot')
    plt.xlabel('Number of Comments')
    plt.ylabel('Interaction')
    plt.grid(True)
    plt.tight_layout()
    

    with tempfile.NamedTemporaryFile(suffix='.png', dir=TEMP_DIR, delete=False) as temp_file:
        temp_file_path = temp_file.name
        plt.savefig(temp_file_path)
    
    # Return the path to the generated line plot image file
    return temp_file_path
    # # Save the plot as an image file
    # plt.savefig('line_plot.png')
    # plt.close()
    
    # # Return the path to the generated line plot image file
    # return 'line_plot.png'
