def create_network_graph(authors, interactions):
    # Creating a directed graph for user interactions
    G = nx.DiGraph()

    # Extracting user interactions from the provided data
    for author in authors:
        G.add_node(author)

    for interaction in interactions:
        if interaction[1]:  # If there's a comment body
            G.add_edge(interaction[0], interaction[1])

    # Visualizing the network graph
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, with_labels=False, node_size=100, node_color="orange", edge_color="gray", width=0.5)
    plt.title(f'User Interaction Network')
    plt.show()

# Example usage
authors = ["author1", "author2", "author3"]
interactions = [("author1", "author2"), ("author2", "author3"), ("author1", "author3")]
create_network_graph(authors, interactions)
