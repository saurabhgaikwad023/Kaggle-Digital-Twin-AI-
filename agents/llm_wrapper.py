# agents/llm_wrapper.py
class MockLLM:
    def explain(self, plan_row):
        return (f"This plan yields productivity={plan_row['productivity']:.1f}, stress={plan_row['stress']:.1f}, "
                f"cost=${plan_row['cost']:.2f}. Recommendation: keep work_hours={plan_row['work_hours']} and "
                f"self_care_hours={plan_row['self_care_hours']} to balance stress and productivity.")
