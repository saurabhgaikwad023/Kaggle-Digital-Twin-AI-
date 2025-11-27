import json, os, time

class MemoryBank:
    def __init__(self, path: str = None):
        self.path = path
        self.store = {}
        if path and os.path.exists(path):
            try:
                with open(path) as f:
                    self.store = json.load(f)
            except Exception:
                self.store = {}

    def save_user(self, uid:str, data:dict):
        self.store[uid] = data
        self._persist()

    def get_user(self, uid:str):
        return self.store.get(uid, {})

    def log_episode(self, uid:str, eid:str, result:dict):
        self.store.setdefault(uid, {}).setdefault('episodes', {})[eid] = {'ts': time.time(), 'result': result}
        self._persist()

    def _persist(self):
        if not self.path:
            return
        try:
            with open(self.path, 'w') as f:
                json.dump(self.store, f)
        except Exception:
            pass
