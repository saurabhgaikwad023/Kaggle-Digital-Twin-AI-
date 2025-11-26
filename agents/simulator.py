import pandas as pd

def simulate_week(twin, sc):
    prod = twin.baseline_productivity + 2.5*sc['work_hours'] + 0.5*sc['social_events'] - 4*max(0, sc['commute_variation'])
    stress = twin.baseline_stress + 0.6*sc['work_hours'] - 0.9*sc['self_care_hours'] + 2*max(0, sc['commute_variation'])
    commute = twin.commute_hours + sc['commute_variation']
    social = twin.social_need + 0.8*sc['social_events']
    cost = twin.budget + sc['budget_change'] - (sc['social_events']*4)
    return {
        "scenario_id":sc["id"],
        "productivity":round(max(0,prod),3),
        "stress":round(max(0,stress),3),
        "commute":round(max(0,commute),3),
        "social":round(max(0,social),3),
        "cost":round(max(0,cost),2)
    }

def run_scenarios_for_twin(twin, scenarios):
    return pd.DataFrame([{**sc, **simulate_week(twin,sc)} for sc in scenarios])
