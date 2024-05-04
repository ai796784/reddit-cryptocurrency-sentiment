from flask import Flask, request, Blueprint, send_file
import matplotlib.pyplot as plt

generate_donut_plot = Blueprint('generate_donut_plot', __name__)

@generate_donut_plot.route('/generate_donut_plot', methods=['POST'])
def donut_plot_endpoint():
    # Receive the donut plot data from the PHP request
    donut_plot_data = request.json['donutPlotData']
    
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
    
    # Save the plot as an image file
    plt.savefig('donut_plot.png')
    plt.close()
    
    # Return the path to the generated donut plot image file
    return 'donut_plot.png'

if __name__ == '__main__':
    app.run(debug=True)
