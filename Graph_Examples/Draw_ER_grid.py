import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
import base64


def erdos_renyi_same_n_different_p(n=8, p_values=None, node_size=50, layout_seed=42):
    """
    Create a 2x4 grid of subplots, each an ER random graph on n=100 nodes,
    but with different p values. All nodes are black. A single layout is used
    for all subplots for easy visual comparison. Returns a base64-encoded PNG.
    """
    if p_values is None:
        # Example: 8 p values from sparse to complete
        p_values = [0.009, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8, 1.0]

    # Prepare a 2x4 grid (8 subplots)
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.flatten()

    # We'll compute a single layout for n=100 nodes
    # so that node positions don't jump around between subplots.
    # Start with an empty graph just to define the nodes:
    full_graph = nx.empty_graph(n)
    pos = nx.spring_layout(full_graph, seed=layout_seed, k=1.0, scale=2.0)

    for ax, p in zip(axes, p_values):
        # Generate a random graph G(n, p). Use a seed for reproducibility.
        G = nx.gnp_random_graph(n, p, seed=int(p * 1000) + layout_seed)

        # Draw edges
        nx.draw_networkx_edges(
            G, pos, ax=ax, edgelist=G.edges(), width=1.5, edge_color="black"
        )

        # Draw nodes (all black)
        nx.draw_networkx_nodes(
            G, pos, ax=ax, node_color="black", node_size=node_size, edgecolors="black"
        )

        # Title with p value
        ax.set_title(f"p = {p}", fontsize=20)

        # Show bounding box: keep axis ON, remove ticks, make spines black
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_edgecolor("black")
            spine.set_linewidth(1)

    plt.tight_layout()

    # Save figure to in-memory buffer
    buf = BytesIO()
    plt.savefig(buf, format="pdf", bbox_inches="tight")
    buf.seek(0)

    # Convert to base64 for direct embedding (optional)
    return base64.b64encode(buf.read()).decode("utf-8")


if __name__ == "__main__":
    # Run it and generate the 8-subplot figure
    img_data = erdos_renyi_same_n_different_p(
        n=8,
        p_values=[0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.8, 1.0],
        node_size=50,
        layout_seed=42,
    )

    # Option 1: Save PNG to disk
    with open("erdos_renyi_100_nodes_different_p.png", "wb") as f:
        f.write(base64.b64decode(img_data))

    # Option 2: Print Base64 (so you can embed it in an <img> tag)
    print(img_data)
