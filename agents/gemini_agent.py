import json, os
from .agent_core import Agent

def build_gemini_client():
    try:
        from google import genai
    except Exception:
        raise RuntimeError('google-genai not installed')
    if not os.environ.get('GEMINI_API_KEY'):
        raise RuntimeError('GEMINI_API_KEY not set')
    return genai.Client(api_key=os.environ['GEMINI_API_KEY'])

class GeminiAgent(Agent):
    def __init__(self, id:str, client, model:str='gemini-2.0-flash', tools:dict=None):
        super().__init__(id, tools=tools); self.client = client; self.model = model

    def explain(self, plan:dict) -> str:
        prompt = ('Explain this weekly plan in 2 short sentences. Mention tradeoffs between productivity, stress, and cost.\n\n' + json.dumps(plan, indent=2))
        resp = self.client.models.generate_content(model=self.model, contents=prompt)
        if hasattr(resp, 'text') and resp.text: return resp.text.strip()
        try:
            return resp.candidates[0].content.parts[0].text
        except Exception:
            return str(resp)

    def act(self, ctx:dict) -> dict:
        plan = ctx.get('plan') or {}
        return {'explanation': self.explain(plan)}
