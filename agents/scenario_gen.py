import random
from typing import List, Dict
from .twin import UserTwin

RANDOM_SEED = 123

def generate_scenarios(twin: UserTwin, n:int=80, seed:int=None) -> List[Dict]:
    if seed is not None:
        random.seed(seed)
    scenarios = []
    for i in range(n):
        scenarios.append({
            'id': f'sc_{i}',
            'work_hours': random.randint(4,10),
            'commute_variation': random.uniform(-0.5,1.5),
            'social_events': random.randint(0,4),
            'self_care_hours': round(random.uniform(0,6),1),
            'budget_change': round(random.uniform(-50,100),1)
        })
    print(f'[scenario_gen] Generated {n} scenarios (seed={seed}).')
    return scenarios
