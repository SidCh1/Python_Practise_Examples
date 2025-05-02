import networkx as nx
import itertools

# Uncomment the next two lines if you have tqdm installed for a progress bar.
from tqdm import tqdm

edge_combinations = tqdm(
    list(itertools.combinations(range(7), 2)), desc="Edge combinations"
)

# Define the nodes and all possible edges (undirected, no self-loops)
nodes = list(range(7))
all_possible_edges = list(itertools.combinations(nodes, 2))

# List to store unique (non-isomorphic) graphs that satisfy the conditions
unique_graphs = []

# Counters for reporting
count_valid = (
    0  # count of graphs meeting the conditions (may include isomorphic duplicates)
)

# Iterate over all 9-edge subsets (each is a candidate graph)
for edge_subset in itertools.combinations(all_possible_edges, 9):
    # Create a graph with the given nodes and edge subset
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edge_subset)

    # Check if the graph is connected
    if not nx.is_connected(G):
        continue

    # Count how many nodes have degree 3
    degree_3_count = sum(1 for node, deg in G.degree() if deg == 3)
    if degree_3_count != 3:
        continue

    # This graph meets the criteria
    count_valid += 1

    # Check if it is isomorphic to any graph we have already found
    is_new = True
    for H in unique_graphs:
        if nx.is_isomorphic(G, H):
            is_new = False
            break
    if is_new:
        unique_graphs.append(G)
    print(len(unique_graphs))

print("Total number of valid graphs (including isomorphic copies):", count_valid)
print("Number of unique graphs (up to isomorphism):", len(unique_graphs))
