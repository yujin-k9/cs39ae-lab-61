import networkx as nx
import pandas as pd

def compute_degree_centrality(G):
    result = nx.degree_centrality(G)
    df = pd.DataFrame(result.items(), columns=["node", "degree"])
    return df

def compute_betweenness_centrality(G):
    result = nx.betweenness_centrality(G)
    df = pd.DataFrame(result.items(), columns=["node", "betweenness"])
    return df

def compute_closeness_centrality(G):
    result = nx.closeness_centrality(G)
    df = pd.DataFrame(result.items(), columns=["node", "closeness"])
    return df
