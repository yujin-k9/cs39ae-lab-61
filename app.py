import streamlit as st
import pandas as pd
from analysis.graph_builder import load_graph, build_pyvis_graph
from analysis.centrality import compute_degree_centrality, compute_betweenness_centrality, compute_closeness_centrality
from analysis.community import detect_communities
from analysis.influence import find_most_influential

st.title("Friendship Network Analysis")

file_path = "data/friendships.csv"
G = load_graph(file_path)

degree_df = compute_degree_centrality(G)
bet_df = compute_betweenness_centrality(G)
close_df = compute_closeness_centrality(G)
community_df = detect_communities(G)

influential = find_most_influential(degree_df, bet_df, close_df)

st.subheader("Most influential person")
st.write(influential)

html_path = "network_graph.html"
build_pyvis_graph(G, html_path, influential)


st.subheader("Network graph")
with open(html_path, "r") as f:
    graph_html = f.read()
st.components.v1.html(graph_html, height=600, scrolling=True)

st.subheader("Degree centrality (descending order)")
st.dataframe(degree_df)

st.subheader("Betweenness centrality (descending order)")
st.dataframe(bet_df)

st.subheader("Closeness centrality (descending order)")
st.dataframe(close_df)

st.subheader("Community groups")
st.dataframe(community_df)
