# from notion_client import Client
# from collections import defaultdict

# # Optional: for graph drawing
# import networkx as nx
# import matplotlib.pyplot as plt

# # Replace with your integration token
# notion = Client(auth="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")


# # --- Step 1: Get all databases ---
# def get_all_databases(max_pages=10):
#     databases = {}
#     cursor = None
#     page_count = 0

#     print("🔍 Searching for databases...")

#     while page_count < max_pages:
#         response = notion.search(
#             filter={"property": "object", "value": "database"},
#             start_cursor=cursor,
#             page_size=20,
#         )
#         for db in response["results"]:
#             db_id = db["id"]
#             title = db.get("title", [])
#             if title:
#                 db_name = title[0]["text"]["content"]
#             else:
#                 db_name = "Untitled"
#             databases[db_id] = db_name

#         page_count += 1
#         if not response.get("has_more"):
#             break
#         cursor = response["next_cursor"]

#     if page_count == max_pages:
#         print(f"⚠️ Stopped after {max_pages} pages to avoid infinite loop.")
#     print(f"✅ Found {len(databases)} databases.")
#     return databases


# # --- Step 2: Find database relation links ---
# def find_relations(databases):
#     links = defaultdict(list)
#     print("🔗 Scanning for relations between databases...")
#     for db_id, db_name in databases.items():
#         try:
#             db_props = notion.databases.retrieve(database_id=db_id)["properties"]
#             for prop_name, prop_info in db_props.items():
#                 if prop_info["type"] == "relation":
#                     related_db_id = prop_info["relation"]["database_id"]
#                     links[db_id].append((prop_name, related_db_id))
#         except Exception as e:
#             print(f"⚠️ Error reading '{db_name}': {e}")
#     return links


# # --- Step 3: Print readable summary ---
# def print_links(databases, links):
#     for db_id, relations in links.items():
#         db_name = databases.get(db_id, db_id)
#         print(f"\n📄 {db_name} is linked to:")
#         for prop_name, related_id in relations:
#             related_name = databases.get(related_id, related_id)
#             print(f"  🔁 {related_name} via relation '{prop_name}'")


# # --- Optional: Step 4: Visualize the database relation graph ---
# def draw_graph(databases, links):
#     G = nx.DiGraph()
#     for db_id, db_name in databases.items():
#         G.add_node(db_name)
#     for db_id, relations in links.items():
#         for _, related_id in relations:
#             if db_id in databases and related_id in databases:
#                 G.add_edge(databases[db_id], databases[related_id])

#     plt.figure(figsize=(10, 6))
#     nx.draw_networkx(
#         G,
#         with_labels=True,
#         node_color="lightgreen",
#         edge_color="gray",
#         node_size=2000,
#         font_size=10,
#         arrows=True,
#     )
#     plt.title("Notion Database Relation Graph")
#     plt.axis("off")
#     plt.tight_layout()
#     plt.show()


# # --- Run the tool ---
# if __name__ == "__main__":
#     databases = get_all_databases()
#     if not databases:
#         print("⚠️ No databases found. Make sure the integration has access.")
#     else:
#         links = find_relations(databases)
#         print_links(databases, links)

#         draw = (
#             input("\nWould you like to visualize the database graph? (y/n): ")
#             .strip()
#             .lower()
#         )
#         if draw == "y":
#             draw_graph(databases, links)


from notion_client import Client
from collections import defaultdict
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Your Notion integration token
# notion = Client(auth="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")

notion = Client(auth="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")


# --- Step 1: Get all databases ---
def get_all_databases(max_pages=10):
    databases = {}
    cursor = None
    page_count = 0

    print("🔍 Searching for databases...")
    while page_count < max_pages:
        response = notion.search(
            filter={"property": "object", "value": "database"},
            start_cursor=cursor,
            page_size=20,
        )
        for db in response["results"]:
            db_id = db["id"]
            title = db.get("title", [])
            db_name = title[0]["text"]["content"] if title else "Untitled"
            databases[db_id] = db_name
        page_count += 1
        if not response.get("has_more"):
            break
        cursor = response["next_cursor"]

    print(f"✅ Found {len(databases)} databases.")
    return databases


# --- Step 2: Get all pages (to look for views) ---
def get_all_pages(max_pages=20):
    pages = {}
    cursor = None
    page_count = 0

    print("📄 Searching for pages...")
    while page_count < max_pages:
        response = notion.search(
            filter={"value": "page", "property": "object"},
            start_cursor=cursor,
            page_size=20,
        )
        for page in response["results"]:
            page_id = page["id"]
            title = "Untitled"
            try:
                props = page.get("properties", {})
                for val in props.values():
                    if val.get("type") == "title":
                        title_items = val.get("title", [])
                        if title_items:
                            title = title_items[0]["text"]["content"]
                            break
            except:
                pass
            pages[page_id] = title
        page_count += 1
        if not response.get("has_more"):
            break
        cursor = response["next_cursor"]

    print(f"📦 Found {len(pages)} pages.")
    return pages


# --- Step 3: Find relation properties in databases ---
def find_relations(databases):
    links = []
    for db_id, db_name in databases.items():
        try:
            db_props = notion.databases.retrieve(database_id=db_id)["properties"]
            for prop_name, prop_info in db_props.items():
                if prop_info["type"] == "relation":
                    related_db_id = prop_info["relation"]["database_id"]
                    links.append(
                        {
                            "source_type": "database",
                            "source_name": db_name,
                            "source_id": db_id,
                            "relation_name": prop_name,
                            "target_name": databases.get(related_db_id, "Unknown"),
                            "target_id": related_db_id,
                            "link_type": "relation",
                        }
                    )
        except Exception as e:
            print(f"⚠️ Error reading '{db_name}': {e}")
    return links


# --- Step 4: Detect linked database views in pages ---
def find_linked_views(databases, pages):
    views = []
    for page_id, page_name in pages.items():
        try:
            children = notion.blocks.children.list(page_id, page_size=100)["results"]
            for block in children:
                if block["type"] == "child_database":
                    db_id = block["id"]
                    views.append(
                        {
                            "source_type": "page",
                            "source_name": page_name,
                            "source_id": page_id,
                            "relation_name": "(linked view)",
                            "target_name": block["child_database"].get(
                                "title", "Embedded DB"
                            ),
                            "target_id": db_id,
                            "link_type": "linked_view",
                        }
                    )
                elif block["type"] == "linked_database":
                    target_id = block["linked_database"]["database_id"]
                    views.append(
                        {
                            "source_type": "page",
                            "source_name": page_name,
                            "source_id": page_id,
                            "relation_name": "(linked view)",
                            "target_name": databases.get(target_id, "Unknown"),
                            "target_id": target_id,
                            "link_type": "linked_view",
                        }
                    )
        except Exception as e:
            print(f"⚠️ Could not read page '{page_name}': {e}")
    return views


# --- Step 5: Export links to CSV ---
def export_links_csv(all_links, filename="notion_database_links.csv"):
    df = pd.DataFrame(all_links)
    df.to_csv(filename, index=False)
    print(f"📁 Exported {len(df)} connections to {filename}")


# --- Step 6: (Optional) Visualize the database graph ---
def draw_graph(all_links):
    G = nx.DiGraph()
    for link in all_links:
        G.add_node(link["source_name"])
        G.add_node(link["target_name"])
        label = link["relation_name"]
        G.add_edge(link["source_name"], link["target_name"], label=label)

    pos = nx.spring_layout(G, k=0.8)
    edge_labels = nx.get_edge_attributes(G, "label")

    plt.figure(figsize=(12, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightgreen",
        node_size=2000,
        edge_color="gray",
        font_size=9,
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title("🔗 Notion Database Connection Graph")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    databases = get_all_databases()
    print("\n📚 List of all databases found:")
    for db_id, db_name in databases.items():
        print(f"• {db_name} ({db_id})")

    pages = get_all_pages()
    relation_links = find_relations(databases)
    view_links = find_linked_views(databases, pages)
    all_links = relation_links + view_links

    # Show summary
    for link in all_links:
        print(
            f"{link['source_name']} → {link['target_name']} [{link['link_type']}] via '{link['relation_name']}'"
        )

    export_links_csv(all_links)

    draw = input("\n📊 Visualize graph? (y/n): ").strip().lower()
    if draw == "y":
        draw_graph(all_links)
