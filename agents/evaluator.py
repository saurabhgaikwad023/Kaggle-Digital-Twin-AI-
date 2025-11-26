import numpy as np
import pandas as pd

def summarize_df(df):
    return {
        "avg_productivity":float(df["productivity"].mean()),
        "avg_stress":float(df["stress"].mean()),
        "avg_commute":float(df["commute"].mean()),
        "avg_cost":float(df["cost"].mean()),
    }

def pareto_front(df):
    if df.empty: return df
    vals=df[["productivity","stress","cost"]].values.astype(float)
    vals[:,0]*=-1
    n=len(vals)
    keep=np.ones(n,bool)
    for i in range(n):
        if not keep[i]: continue
        dominated=(np.all(vals<=vals[i],1)&np.any(vals<vals[i],1))
        dominated[i]=False
        if dominated.any(): keep[i]=False
    return df[keep].reset_index(drop=True)

def choose_plans(df,k=5):
    if df.empty: return df
    d=df.copy()
    for c in ["productivity","stress","cost"]:
        mn, mx = d[c].min(), d[c].max()
        d[c+"_n"] = (d[c]-mn)/((mx-mn) if mx!=mn else 1e-9)
    d["score"]=d["productivity_n"] - d["stress_n"] - d["cost_n"]
    return d.sort_values("score",ascending=False).head(k).reset_index(drop=True)
