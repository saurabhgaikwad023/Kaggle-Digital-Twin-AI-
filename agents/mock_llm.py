class MockLLM:
    def explain(self,row):
        return (f"Prod={row['productivity']}, Stress={row['stress']}, Cost={row['cost']} — "
                f"Keep work_hours={row['work_hours']} & self_care={row['self_care_hours']}")
