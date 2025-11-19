import networkx as nx
import pandas as pd

def detect_communities(G):
    communities = nx.community.greedy_modularity_communities(G)
    result = []

    for idx, group in enumerate(communities):
        for node in group:
            result.append({"node": node, "community": idx})

    df = pd.DataFrame(result)
    return df
