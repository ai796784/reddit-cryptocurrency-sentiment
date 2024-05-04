from flask import Flask, request, Blueprint, send_file
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

generate_heat_plot = Blueprint('generate_heat_plot', __name__)

@generate_heat_plot.route('/generate_heat_plot', methods=['POST'])
def heat_plot_endpoint():
    # Receive the heat plot data from the PHP request
    heat_plot_data = request.json['heatPlotData']
    
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(heat_plot_data)
    
    # Generate the heat plot
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title('Heat Plot')
    plt.tight_layout()
    
    # Save the plot as an image file
    plt.savefig('heat_plot.png')
    plt.close()
    
    # Return the path to the generated heat plot image file
    return 'heat_plot.png'

if __name__ == '__main__':
    app.run(debug=True)
