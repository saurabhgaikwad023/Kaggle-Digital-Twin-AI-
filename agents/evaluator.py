# agents/evaluator.py
import numpy as np
import pandas as pd

def summarize_df(df:pd.DataFrame):
    return {
        'avg_productivity': float(df['productivity'].mean()),
        'avg_stress': float(df['stress'].mean()),
        'avg_commute': float(df['commute'].mean()),
        'avg_cost': float(df['cost'].mean())
    }

def pareto_front(df:pd.DataFrame, objs=None):
    if objs is None:
        objs = [('productivity','max'), ('stress','min'), ('cost','min')]
    vals = df[[o[0] for o in objs]].values.astype(float).copy()
    for i,(name,typ) in enumerate(objs):
        if typ == 'max':
            vals[:,i] = -vals[:,i]
    is_pareto = np.ones(vals.shape[0], dtype=bool)
    for i, v in enumerate(vals):
        if not is_pareto[i]:
            continue
        compare = np.any((vals <= v) & (np.any(vals < v, axis=1)[:,None]), axis=1)
        compare[i] = False
        if np.any(compare):
            is_pareto[i] = False
    return df[is_pareto].reset_index(drop=True)
