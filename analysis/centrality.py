import networkx as nx
import pandas as pd

def compute_degree_centrality(G):
    degree_dict = dict(G.degree()) 
    df = pd.DataFrame(degree_dict.items(), columns=["node", "degree"])
    df = df.sort_values("degree", ascending=False).reset_index(drop=True)
    return df

def compute_betweenness_centrality(G):
    result = nx.betweenness_centrality(G)
    df = pd.DataFrame(result.items(), columns=["node", "betweenness"])
    df = df.sort_values("betweenness", ascending=False).reset_index(drop=True)
    return df

def compute_closeness_centrality(G):
    result = nx.closeness_centrality(G)
    df = pd.DataFrame(result.items(), columns=["node", "closeness"])
    df = df.sort_values("closeness", ascending=False).reset_index(drop=True)
    return df
