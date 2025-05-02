import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64


def waxman_graph(n, alpha=0.5, beta=1.0, pos=None, rng=None):
    """
    Generate a Waxman graph on n nodes with edge probability:
         P(e_{ij}) = beta * exp( -d(i,j) / (alpha * L) )
    where d(i,j) is the Euclidean distance between nodes i and j,
    and L is the maximum distance among all node pairs.
    """
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
    L = max(distances) if distances else 1

    G = nx.empty_graph(n)
    for i in range(n):
        for j in range(i + 1, n):
            d = np.linalg.norm(np.array(pos[i]) - np.array(pos[j]))
            prob = beta * np.exp(-d / (alpha * L))
            if rng.random() < prob:
                G.add_edge(i, j)
    return G


def waxman_vary_alpha(alphas, n=80, beta=1.0, node_size=100, seed=42):
    """
    Create a grid of subplots where each subplot shows a Waxman graph
    with n nodes (here fixed at 80) and a different alpha value.
    The title of each box displays the alpha value and the largest connected
    component (LCC) size over the total number of nodes.
    """
    num_plots = len(alphas)
    rows = 2
    cols = (num_plots + 1) // 2  # rounds up if needed
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 4, rows * 4))
    axes = axes.flatten() if isinstance(axes, np.ndarray) else [axes]

    rng = np.random.default_rng(seed)
    # Compute fixed positions for all n nodes
    pos_full = {i: rng.random(2) for i in range(n)}

    for ax, alpha in zip(axes, alphas):
        pos = {i: pos_full[i] for i in range(n)}
        G = waxman_graph(n, alpha=alpha, beta=beta, pos=pos, rng=rng)

        # Draw edges and nodes (all in black)
        nx.draw_networkx_edges(G, pos, ax=ax, edge_color="black", width=1.5)
        nx.draw_networkx_nodes(
            G, pos, ax=ax, node_color="black", node_size=node_size, edgecolors="black"
        )

        # Compute size of the largest connected component (LCC)
        if G.number_of_edges() > 0:
            largest_cc = max(nx.connected_components(G), key=len)
            lcc_size = len(largest_cc)
        else:
            lcc_size = 1  # if no edges, each node is isolated

        ax.set_title(
            f"α = {alpha}\nLCC: {lcc_size}/{n}", fontsize=16, fontweight="bold"
        )
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_edgecolor("black")
            spine.set_linewidth(1)

    # Turn off any unused axes
    for j in range(len(alphas), len(axes)):
        axes[j].axis("off")

    plt.tight_layout()

    # Save the figure into an in-memory buffer and return a Base64 string
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")


if __name__ == "__main__":
    # Example: vary alpha over 8 values
    alphas = [0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.09, 0.1]
    img_data = waxman_vary_alpha(alphas, n=80, beta=1.0, node_size=100, seed=42)

    # Option 1: Save the image locally
    with open("waxman_vary_alpha.png", "wb") as f:
        f.write(base64.b64decode(img_data))

    # Option 2: Print the Base64 string (for embedding)
    print(img_data)
