# agents/simulator.py
import random
import pandas as pd

def simulate_week(twin, scenario):
    productivity = (twin.baseline_productivity 
                    + 2.5 * scenario['work_hours'] 
                    + 0.5 * scenario['social_events']
                    - 0.8 * max(0, scenario['commute_variation'])*5)
    stress = (twin.baseline_stress 
              + 0.6 * scenario['work_hours'] 
              - 0.9 * scenario['self_care_hours'] 
              + 0.4 * max(0, scenario['commute_variation'])*5)
    commute = twin.commute_hours + scenario['commute_variation']
    social = twin.social_need + 0.8 * scenario['social_events']
    cost = twin.budget + scenario['budget_change'] - (0.2 * scenario['social_events']*20)
    productivity = max(0, productivity)
    stress = max(0, stress)
    commute = max(0, commute)
    social = max(0, social)
    cost = max(0, cost)
    return {
        'scenario_id': scenario['id'],
        'productivity': round(productivity,3),
        'stress': round(stress,3),
        'commute': round(commute,3),
        'social': round(social,3),
        'cost': round(cost,2)
    }

def run_scenarios_for_twin(twin, scenarios):
    rows = []
    for sc in scenarios:
        out = simulate_week(twin, sc)
        merged = {**sc, **out}
        rows.append(merged)
    return pd.DataFrame(rows)
