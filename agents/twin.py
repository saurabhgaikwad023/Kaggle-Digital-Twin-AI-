from dataclasses import dataclass

@dataclass
class UserTwin:
    id: str
    baseline_productivity: float
    baseline_stress: float
    commute_hours: float
    social_need: float
    budget: float
