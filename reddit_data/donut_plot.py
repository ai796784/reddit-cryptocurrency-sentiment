from flask import Flask, request, Blueprint, send_file
import matplotlib.pyplot as plt
import tempfile


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
    
    # Generate the donut plot
    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Donut Plot')
    plt.tight_layout()
    
    # Draw a circle at the center to make it a donut plot
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    

    with tempfile.NamedTemporaryFile(suffix='.png', dir=TEMP_DIR, delete=False) as temp_file:
        temp_file_path = temp_file.name
        plt.savefig(temp_file_path)
    
    # Return the path to the generated line plot image file
    return temp_file_path
    # # Save the plot as an image file
    # plt.savefig('donut_plot.png')
    # plt.close()
    
    # # Return the path to the generated donut plot image file
    # return 'donut_plot.png'

