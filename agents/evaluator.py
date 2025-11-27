import numpy as np
import pandas as pd
from typing import Dict

def summarize_df(df: pd.DataFrame) -> Dict:
    s = {
        'avg_productivity': float(df['productivity'].mean()),
        'avg_stress': float(df['stress'].mean()),
        'avg_commute': float(df['commute'].mean()),
        'avg_cost': float(df['cost'].mean())
    }
    print('[evaluator] summarize_df ready')
    return s

def pareto_front(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame()
    vals = df[['productivity','stress','cost']].values.astype(float).copy()
    vals[:,0] = -vals[:,0]  # maximize productivity
    n = vals.shape[0]
    keep = np.ones(n, dtype=bool)
    for i in range(n):
        if not keep[i]:
            continue
        dominated = np.all(vals <= vals[i], axis=1) & np.any(vals < vals[i], axis=1)
        dominated[i] = False
        if np.any(dominated):
            keep[i] = False
    print(f'[evaluator] Pareto computed: kept {keep.sum()} of {n}')
    return df[keep].reset_index(drop=True)

def choose_plans(pf: pd.DataFrame, k:int=5) -> pd.DataFrame:
    if pf is None or pf.empty:
        return pd.DataFrame()
    df = pf.copy()
    def sr(col):
        mn, mx = df[col].min(), df[col].max()
        return mn, (mx - mn) if mx != mn else 1e-9
    pmin, pr = sr('productivity'); smin, srng = sr('stress'); cmin, cr = sr('cost')
    df['score'] = ((df['productivity']-pmin)/pr) - ((df['stress']-smin)/srng) - ((df['cost']-cmin)/cr)
    print(f'[evaluator] choose_plans scored {len(df)} plans; returning top {k}')
    return df.sort_values('score', ascending=False).head(k).reset_index(drop=True)
