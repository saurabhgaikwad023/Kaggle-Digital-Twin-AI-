from typing import Dict, List
import pandas as pd
from .twin import UserTwin

def simulate_week(twin: UserTwin, scenario: Dict) -> Dict:
    productivity = (
        twin.baseline_productivity
        + 2.5 * scenario['work_hours']
        + 0.5 * scenario['social_events']
        - 4 * max(0, scenario['commute_variation'])
    )

    stress = (
        twin.baseline_stress
        + 0.6 * scenario['work_hours']
        - 0.9 * scenario['self_care_hours']
        + 2 * max(0, scenario['commute_variation'])
    )

    commute = max(0.0, twin.commute_hours + scenario['commute_variation'])
    social = max(0.0, twin.social_need + 0.8 * scenario['social_events'])
    cost = max(0.0, twin.budget + scenario['budget_change'] - scenario['social_events'] * 4)

    return {
        'scenario_id': scenario['id'],
        'productivity': round(max(0.0, productivity), 3),
        'stress': round(max(0.0, stress), 3),
        'commute': round(commute, 3),
        'social': round(social, 3),
        'cost': round(cost, 2),
    }


def run_scenarios_for_twin(twin: UserTwin, scenarios: List[Dict]) -> pd.DataFrame:
    rows = []
    for sc in scenarios:
        rows.append({**sc, **simulate_week(twin, sc)})
    return pd.DataFrame(rows)
