from flask import Flask, request, Blueprint, send_file
import matplotlib.pyplot as plt
import networkx as nx

generate_network_plot = Blueprint('generate_network_plot', __name__)

@network_plot.route('/generate_network_plot', methods=['POST'])
def network_plot_endpoint():
    # Receive the network plot data from the PHP request
    network_plot_data = request.json['networkPlotData']
    
    # Extract nodes and edges from the received data
    nodes = network_plot_data['nodes']
    edges = network_plot_data['edges']
    
    # Create a networkx graph
    G = nx.Graph()
    
    # Add nodes to the graph
    for node in nodes:
        G.add_node(node['id'], label=node['label'])
    
    # Add edges to the graph
    for edge in edges:
        G.add_edge(edge['from'], edge['to'])
    
    # Generate the network plot
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_weight='bold')
    plt.title('Network Plot')
    plt.tight_layout()
    
    # Save the plot as an image file
    plt.savefig('network_plot.png')
    plt.close()
    
    # Return the path to the generated network plot image file
    return 'network_plot.png'
