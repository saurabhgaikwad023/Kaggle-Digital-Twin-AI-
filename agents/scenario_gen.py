import random

def generate_scenarios(twin, n=80, seed=None):
    if seed:
        random.seed(seed)
    out=[]
    for i in range(n):
        out.append({
            "id":f"sc_{i}",
            "work_hours":random.randint(4,10),
            "commute_variation":random.uniform(-0.5,1.5),
            "social_events":random.randint(0,4),
            "self_care_hours":round(random.uniform(0,6),1),
            "budget_change":round(random.uniform(-50,100),1)
        })
    return out
