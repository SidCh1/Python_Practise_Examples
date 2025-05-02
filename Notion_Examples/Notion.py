# from notion_client import Client
# import os

# notion = Client(auth="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")


# def find_databases(start_cursor=None):
#     databases = []
#     while True:
#         response = notion.search(
#             query="",
#             filter={"property": "object", "value": "database"},
#             start_cursor=start_cursor,
#         )
#         for result in response["results"]:
#             title = (
#                 result["title"][0]["text"]["content"] if result["title"] else "Untitled"
#             )
#             databases.append((title, result["id"]))
#         if response.get("has_more"):
#             start_cursor = response["next_cursor"]
#         else:
#             break
#     return databases


# if __name__ == "__main__":
#     dbs = find_databases()
#     for title, db_id in dbs:
#         print(f"Database: {title}\nID: {db_id}\n")

from notion_client import Client
from collections import defaultdict

# Optional: import for graph drawing
import networkx as nx
import matplotlib.pyplot as plt

# Replace this with your actual integration token
notion = Client(auth="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")


# Get all databases the integration can access
def get_all_databases():
    databases = {}
    cursor = None
    while True:
        response = notion.search(
            filter={"property": "object", "value": "database"},
            start_cursor=cursor,
        )
        for db in response["results"]:
            db_id = db["id"]
            title = db["title"]
            if title:
                db_name = title[0]["text"]["content"]
            else:
                db_name = "Untitled"
            databases[db_id] = db_name
        if not response.get("has_more"):
            break
        cursor = response["next_cursor"]
    return databases


# Scan for relation properties
def find_relations(databases):
    links = defaultdict(list)
    for db_id, db_name in databases.items():
        try:
            db_props = notion.databases.retrieve(database_id=db_id)["properties"]
            for prop_name, prop_info in db_props.items():
                if prop_info["type"] == "relation":
                    related_db_id = prop_info["relation"]["database_id"]
                    links[db_id].append((prop_name, related_db_id))
        except Exception as e:
            print(f"Error reading database {db_name}: {e}")
    return links


# Print readable links
def print_links(databases, links):
    for db_id, relations in links.items():
        db_name = databases.get(db_id, db_id)
        print(f"\n🔗 {db_name} is linked to:")
        for prop_name, related_id in relations:
            related_name = databases.get(related_id, related_id)
            print(f"  - {related_name} via relation '{prop_name}'")


# Optional: draw the link graph
def draw_graph(databases, links):
    G = nx.DiGraph()
    for db_id, db_name in databases.items():
        G.add_node(db_name)
    for db_id, relations in links.items():
        for _, related_id in relations:
            if db_id in databases and related_id in databases:
                G.add_edge(databases[db_id], databases[related_id])

    plt.figure(figsize=(10, 6))
    nx.draw_networkx(
        G,
        with_labels=True,
        node_color="lightgreen",
        edge_color="gray",
        node_size=2000,
        font_size=10,
    )
    plt.title("Database Relation Graph")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# Run it all
if __name__ == "__main__":
    print("🔍 Scanning Notion workspace...")
    databases = get_all_databases()
    links = find_relations(databases)
    print_links(databases, links)

    draw = (
        input("\nWould you like to visualize the database graph? (y/n): ")
        .strip()
        .lower()
    )
    if draw == "y":
        draw_graph(databases, links)
