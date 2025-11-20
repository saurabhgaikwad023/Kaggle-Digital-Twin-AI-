# agents/twin_builder.py
from dataclasses import dataclass

@dataclass
class UserTwin:
    id: str
    baseline_productivity: float
    baseline_stress: float
    commute_hours: float
    social_need: float
    budget: float

class TwinBuilder:
    @staticmethod
    def build_from_profile(pid:str, profile:dict):
        return UserTwin(
            id=pid,
            baseline_productivity=profile.get('baseline_productivity',40),
            baseline_stress=profile.get('baseline_stress',15),
            commute_hours=profile.get('commute_hours',1.0),
            social_need=profile.get('social_need',2.0),
            budget=profile.get('budget',300)
        )
