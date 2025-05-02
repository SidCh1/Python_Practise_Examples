import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Define the 7-node hexagonal graph with a center node (node 6)
hexagon_edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]  # Hexagon perimeter
center_edges = [(6, i) for i in range(6)]  # Center node connections

# Initial full graph
G = nx.Graph()
G.add_edges_from(hexagon_edges + center_edges)

# Generate adjacency matrices with progressive edge removal
edge_removal_steps = [hexagon_edges[:i] for i in range(len(hexagon_edges) + 1)]

# Directory to store CSV files
csv_files = []

# Visualization setup
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

# Layout for consistent visualization
pos = nx.spring_layout(G, seed=42)

for i, edges_to_remove in enumerate(edge_removal_steps):
    # Create graph copy and remove edges
    G_mod = G.copy()
    G_mod.remove_edges_from(edges_to_remove)

    # Compute adjacency matrix
    adj_matrix = nx.to_numpy_array(G_mod, dtype=int)

    # Save to CSV file
    csv_filename = f"./hex_graph_{i}.csv"
    np.savetxt(csv_filename, adj_matrix, delimiter=";", fmt="%d")
    csv_files.append(csv_filename)

    # Plot graph
    if i < len(axes):  # Limit plots to available subplot space
        ax = axes[i]
        nx.draw(
            G_mod,
            pos,
            with_labels=True,
            node_color="lightblue",
            edge_color="black",
            ax=ax,
        )
        ax.set_title(f"Edges Removed: {i}")

# Show plots
plt.tight_layout()
plt.show()

# Return list of saved CSV files
csv_files
