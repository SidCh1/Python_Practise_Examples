# This program calculates the height of a tree with alternating branching factors using two methods:
# 1. **Iterative Method**:
#    - The tree starts with a root node at level 0.
#    - Each level alternates between two branching factors (`multiplier1` and `multiplier2`).
#    - Nodes at each level are calculated iteratively, and the process stops once the total number of nodes
#      reaches or exceeds the specified limit (`total_nodes`).
#    - This method provides an exact height of the tree by counting the levels explicitly.
#
# 2. **Formula-Based Approximation**:
#    - The height is estimated using the formula:
#          h ≈ (2 * log(N)) / (log(x) + log(y))
#      where:
#          N = Total number of nodes in the tree,
#          x = First branching factor (`multiplier1`),
#          y = Second branching factor (`multiplier2`).
#    - This formula assumes a uniform distribution of growth and provides an approximate result
#      based on logarithmic calculations.
#
# Inputs:
# - `total_nodes`: Total number of nodes in the tree.
# - `multiplier1`: First branching factor (e.g., 2).
# - `multiplier2`: Second branching factor (e.g., 3).
#
# Outputs:
# - Iterative height of the tree (exact value).
# - Distribution of nodes at each level (for verification).
# - Approximate height of the tree using the formula (for comparison).
#
# This dual approach helps verify the consistency between the exact calculation and the approximation.

# ===================================================================================================


# Author: Siddardha Chelluri
# Github: SidCh1

# ===================================================================================================


import math


def compute_tree_height(total_nodes, multiplier1, multiplier2):
    nodes_per_level = [1]  # root node at level 0
    current_nodes = 1  # start with the root node
    multiplier = multiplier1  # start with the first multiplier
    level = 0

    # Compute the number of nodes per level until the total reaches or exceeds total_nodes
    while sum(nodes_per_level) < total_nodes:
        current_nodes *= multiplier
        nodes_per_level.append(current_nodes)
        # Alternate the multiplier
        multiplier = multiplier2 if multiplier == multiplier1 else multiplier1
        level += 1

    # The height of the tree is the number of levels (excluding the root level at 0)
    height = len(nodes_per_level) - 1
    return height, nodes_per_level


def approximate_height_formula(total_nodes, multiplier1, multiplier2):
    # Using the formula h ≈ (2 * log(N)) / (log(x) + log(y))
    log_n = math.log10(total_nodes)
    log_x = math.log10(multiplier1)
    log_y = math.log10(multiplier2)
    height = (2 * log_n) / (log_x + log_y)
    return height


# Example usage
total_nodes = 100
multiplier1 = 2  # First multiplier
multiplier2 = 3  # Second multiplier

# Calculate heights
iterative_height, nodes_distribution = compute_tree_height(
    total_nodes, multiplier1, multiplier2
)
formula_height = approximate_height_formula(total_nodes, multiplier1, multiplier2)

# Print results
print(f"Height of the tree (iterative method): {iterative_height}")
print(f"Nodes per level: {nodes_distribution}")
print(f"Height of the tree (formula): {formula_height:.2f}")
