import pandas as pd
import networkx as nx
from pyvis.network import Network

def load_graph(csv_path):
    df = pd.read_csv(csv_path)
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row["source"], row["target"])
    return G

def build_pyvis_graph(G, output_path, highlight_node):
    net = Network(height="600px", width="100 percent", directed=False)

    net.set_options("""
    {
      "physics": {
        "barnesHut": {
          "gravitationalConstant": -9000,
          "centralGravity": 0.3,
          "springLength": 250,
          "springConstant": 0.04,
          "damping": 0.09,
          "avoidOverlap": 1
        }
      }
    }
    """)

    for node in G.nodes():
        if node == highlight_node:
            net.add_node(node, color="red", size=30)
        else:
            net.add_node(node, color="#97C2FC", size=20)

    for edge in G.edges():
        net.add_edge(edge[0], edge[1], color="#97C2FC")

    net.write_html(output_path)
    return output_path
