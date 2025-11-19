import pandas as pd

def find_most_influential(degree_df, bet_df, close_df):
    merged = degree_df.merge(bet_df, on="node")
    merged = merged.merge(close_df, on="node")

    merged["score"] = (
        merged["degree"] +
        merged["betweenness"] +
        merged["closeness"]
    )

    best = merged.sort_values("score", ascending=False).iloc[0]
    return best["node"]
