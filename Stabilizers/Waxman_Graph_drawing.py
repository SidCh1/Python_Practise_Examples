import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64


def waxman_graph(n, p, alpha=0.5, pos=None, rng=None):
    """
    Create a Waxman graph with n nodes. The edge probability between nodes i and j is:
        P(e_{ij}) = p * exp(-d(i,j) / (alpha * L))
    where L is the maximum distance between any two nodes.
    """
    G = nx.empty_graph(n)
    if rng is None:
        rng = np.random.default_rng(42)
    if pos is None:
        pos = {i: rng.random(2) for i in range(n)}

    # Compute maximum distance L among nodes
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            d = np.linalg.norm(np.array(pos[i]) - np.array(pos[j]))
            distances.append(d)
    L = max(distances)

    # For each pair, add an edge with probability = p * exp(-d/(alpha*L))
    for i in range(n):
        for j in range(i + 1, n):
            d = np.linalg.norm(np.array(pos[i]) - np.array(pos[j]))
            edge_prob = p * np.exp(-d / (alpha * L))
            if rng.random() < edge_prob:
                G.add_edge(i, j)
    return G


def waxman_sequence_figure(n=8, p_values=None, node_size=100, alpha=0.5, seed=42):
    """
    Create a 2x4 grid of Waxman model graphs with fixed node positions.
    Each subplot has n nodes (here 8), all black, and the edge probability
    decreases with increasing inter-node distance.
    p_values: List of p parameters (scaling factors) for the Waxman model.
    """
    if p_values is None:
        p_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.flatten()

    # Generate fixed node positions (same for every subplot)
    rng = np.random.default_rng(seed)
    pos = {i: rng.random(2) for i in range(n)}

    for ax, p in zip(axes, p_values):
        # Generate the Waxman graph for this p value.
        G = waxman_graph(n, p, alpha=alpha, pos=pos, rng=rng)

        # Draw edges and nodes (all nodes in black)
        nx.draw_networkx_edges(G, pos, ax=ax, edge_color="black", width=1.5)
        nx.draw_networkx_nodes(
            G, pos, ax=ax, node_color="black", node_size=node_size, edgecolors="black"
        )

        # Title with larger font size
        ax.set_title(f"p = {p}", fontsize=20, fontweight="bold")

        # Remove ticks and add a bounding box by showing spines
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_edgecolor("black")
            spine.set_linewidth(1)

    plt.tight_layout()

    # Save figure to an in-memory buffer and encode as Base64.
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")


if __name__ == "__main__":
    img_data = waxman_sequence_figure(
        n=8,
        p_values=[1.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
        node_size=100,
        alpha=0.5,
        seed=42,
    )

    # Option 1: Save the generated image to a file
    with open("waxman_graphs.png", "wb") as f:
        f.write(base64.b64decode(img_data))

    # Option 2: Print the Base64 string (for embedding in HTML, etc.)
    print(img_data)
