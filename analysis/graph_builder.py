import pandas as pd
import networkx as nx
from pyvis.network import Network

def load_graph(csv_path):
    df = pd.read_csv(csv_path)
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row["source"], row["target"])
    return G

def build_pyvis_graph(G, output_path):
    net = Network(height="600px", width="100 percent", directed=False)
    net.from_nx(G)
    net.write_html(output_path)
    return output_path
