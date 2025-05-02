import networkx as nx
import itertools
from collections import defaultdict


def exact_steiner_tree(G, terminal_nodes):
    """
    Find the exact minimum Steiner tree of a graph with unit weights.

    Parameters:
    -----------
    G : NetworkX graph
        The input graph with unit weights.
    terminal_nodes : list
        A list of terminal nodes for which minimum steiner tree is to be found.

    Returns:
    --------
    NetworkX graph
        The minimum Steiner tree connecting all terminal nodes.
    """
    # Ensure terminal_nodes is a set for efficient membership checking
    terminal_nodes = set(terminal_nodes)

    # Handle edge cases
    if len(terminal_nodes) <= 1:
        tree = nx.Graph()
        for node in terminal_nodes:
            tree.add_node(node)
        return tree

    # Precompute all-pairs shortest paths and path lengths
    all_shortest_paths = dict(nx.all_pairs_shortest_path(G))
    all_shortest_path_lengths = dict(nx.all_pairs_shortest_path_length(G))

    # Initialize the dynamic programming table
    # dp[(frozenset(X), v)] = (cost, partition, u)
    dp = {}

    # Compute the minimum cost Steiner tree for a set of terminals X and a vertex v
    def compute_cost(X, v):
        X_frozen = frozenset(X)
        key = (X_frozen, v)

        if key in dp:
            return dp[key][0]

        if len(X) == 1:
            # Base case: X contains a single terminal t
            t = next(iter(X))
            if t == v:
                dp[key] = (0, None, None)
            elif v in all_shortest_path_lengths.get(t, {}):
                dp[key] = (all_shortest_path_lengths[t][v], None, None)
            else:
                dp[key] = (float("inf"), None, None)
            return dp[key][0]

        if v in X:
            # Special case: v is a terminal in X
            X_without_v = X - {v}
            cost = compute_cost(X_without_v, v)
            dp[key] = (cost, None, None)
            return cost

        # General case: try all bipartitions of X and all vertices u
        min_cost = float("inf")
        best_partition = None
        best_u = None

        for k in range(1, len(X)):
            for X1 in itertools.combinations(X, k):
                X1 = frozenset(X1)
                X2 = X_frozen - X1

                for u in G.nodes():
                    if (
                        u not in all_shortest_path_lengths
                        or v not in all_shortest_path_lengths.get(u, {})
                    ):
                        continue

                    cost1 = compute_cost(X1, u)
                    if cost1 == float("inf"):
                        continue

                    cost2 = compute_cost(X2, u)
                    if cost2 == float("inf"):
                        continue

                    path_cost = all_shortest_path_lengths[u][v]

                    total_cost = cost1 + cost2 + path_cost

                    if total_cost < min_cost:
                        min_cost = total_cost
                        best_partition = (X1, X2)
                        best_u = u

        # Store the result in the dp table
        dp[key] = (min_cost, best_partition, best_u)
        return min_cost

    # Find the best vertex to connect all terminals
    min_cost = float("inf")
    best_v = None

    for v in G.nodes():
        cost = compute_cost(terminal_nodes, v)
        if cost < min_cost:
            min_cost = cost
            best_v = v

    # Construct the minimum Steiner tree
    steiner_tree = nx.Graph()

    # Add all terminal nodes to the tree
    for t in terminal_nodes:
        steiner_tree.add_node(t)

    # Reconstruct the tree using the information in the dp table
    def reconstruct_tree(X, v):
        X_frozen = frozenset(X)
        key = (X_frozen, v)

        if len(X) == 1:
            # Base case: X contains a single terminal t
            t = next(iter(X))
            if t != v:
                path = all_shortest_paths[t][v]
                for i in range(len(path) - 1):
                    u, w = path[i], path[i + 1]
                    steiner_tree.add_edge(u, w)
            return

        if v in X:
            # Special case: v is a terminal in X
            X_without_v = X - {v}
            reconstruct_tree(X_without_v, v)
            return

        # General case: use the information from the dp table
        _, best_partition, best_u = dp[key]

        if best_partition is None:
            return

        X1, X2 = best_partition

        # Add the path from best_u to v
        path = all_shortest_paths[best_u][v]
        for i in range(len(path) - 1):
            u, w = path[i], path[i + 1]
            steiner_tree.add_edge(u, w)

        # Recursively reconstruct the trees for X1 and X2
        reconstruct_tree(X1, best_u)
        reconstruct_tree(X2, best_u)

    # Reconstruct the minimum Steiner tree
    reconstruct_tree(terminal_nodes, best_v)

    return steiner_tree
