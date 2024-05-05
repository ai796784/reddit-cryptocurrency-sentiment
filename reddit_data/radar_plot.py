from flask import Flask, request, Blueprint, send_file
import matplotlib.pyplot as plt
import numpy as np
import tempfile
import os

generate_radar_plot = Blueprint('generate_radar_plot', __name__)

TEMP_DIR = "plots"

@generate_radar_plot.route('/generate_radar_plot', methods=['POST'])
def radar_plot_endpoint():
    # Receive the radar plot data from the PHP request
    radar_plot_data = request.json #['radarPlotData']
    
    radar_plot_data = radar_plot_data[0]

    # Extract labels and values from the received data
    labels = list(radar_plot_data.keys())
    values = list(radar_plot_data.values())
    
    # Number of variables
    num_vars = len(labels)
    
    # Create a list of angles for each variable
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # The radar chart is circular, so we need to "complete the loop" and append the start value to the end.
    values += values[:1]
    angles += angles[:1]
    
    # Generate the radar plot
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='blue', alpha=0.25)
    ax.plot(angles, values, color='blue', linewidth=2)
    
    # Add labels
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    
    # Title
    plt.title('Radar Plot')
    
    # Tight layout
    plt.tight_layout()
    

    with tempfile.NamedTemporaryFile(suffix='.png', dir=TEMP_DIR, delete=False) as temp_file:
        temp_file_path = temp_file.name
        plt.savefig(temp_file_path)
    

    temp_file_path = temp_file.name
    temp_file_name = os.path.basename(temp_file_path)
    
    return temp_file_name  
