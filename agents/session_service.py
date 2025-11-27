import json, os, time

class InMemorySessionService:
    def __init__(self, persist_path: str = None):
        self.sessions = {}
        self.persist_path = persist_path

    def create(self, sid:str, state:dict=None):
        self.sessions[sid] = {'state': state or {}, 'ts': time.time()}

    def get(self, sid:str):
        return self.sessions.get(sid, {}).get('state', {})

    def set(self, sid:str, state:dict):
        self.sessions.setdefault(sid, {})['state'] = state
        self.sessions[sid]['ts'] = time.time()

    def persist(self):
        if not self.persist_path: return
        with open(self.persist_path, 'w') as f:
            json.dump(self.sessions, f)

    def load(self):
        if not self.persist_path or not os.path.exists(self.persist_path): return
        with open(self.persist_path) as f:
            self.sessions = json.load(f)
