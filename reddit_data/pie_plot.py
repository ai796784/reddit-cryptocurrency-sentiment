from flask import Flask, request, Blueprint, send_file
import matplotlib.pyplot as plt

generate_pie_plot = Blueprint('generate_pie_plot', __name__)


@generate_pie_plot.route('/generate_pie_plot', methods=['POST'])
def pie_plot_endpoint():
    # Receive the pie plot data from the PHP request
    pie_plot_data = request.json['piePlotData']
    
    # Extract labels and values from the received data
    labels = list(pie_plot_data.keys())
    values = list(pie_plot_data.values())
    
    # Generate the pie plot
    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title('Pie Plot')
    plt.tight_layout()
    
    # Save the plot as an image file
    plt.savefig('pie_plot.png')
    plt.close()
    
    # Return the path to the generated pie plot image file
    return 'pie_plot.png'

if __name__ == '__main__':
    app.run(debug=True)
