from xml.etree import ElementTree as ET
import matplotlib.pyplot as plt

# Load and parse the SVG file
svg_file_path = "./Rectilinear_minimum_spanning_tree.svg"
tree = ET.parse(svg_file_path)
root = tree.getroot()

# Extract namespace if present
namespace = ""
if "}" in root.tag:
    namespace = root.tag.split("}")[0] + "}"

# Extract all elements from the SVG
elements = list(root.iter())

# Display the first few elements to understand the structure
elements[:10]


# Extract edges from the SVG file
edges = []
node_positions = set()  # To store unique node positions

for element in elements:
    if element.tag == f"{namespace}line":
        x1, y1 = float(element.attrib["x1"]), float(element.attrib["y1"])
        x2, y2 = float(element.attrib["x2"]), float(element.attrib["y2"])

        node_positions.add((x1, y1))
        node_positions.add((x2, y2))
        edges.append(((x1, y1), (x2, y2)))

# Convert node positions to indexed labels
node_list = list(node_positions)
node_mapping = {pos: idx for idx, pos in enumerate(node_list)}

# Convert edges to use indexed labels
edges_labeled = [(node_mapping[u], node_mapping[v]) for u, v in edges]

# Create the NetworkX graph
import networkx as nx

G = nx.Graph()
G.add_edges_from(edges_labeled)

# Display basic info about the graph
# nx.info(G)

plt.figure(figsize=(10, 10))
nx.draw(
    G,
    with_labels=True,
    node_color="lightblue",
    edge_color="gray",
    node_size=100,
    font_size=10,
)
plt.show()
