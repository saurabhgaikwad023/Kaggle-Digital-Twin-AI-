# agents/memory.py
class MemoryBank:
    def __init__(self):
        self.store = {}
    def save_user(self, user_id, data):
        self.store[user_id] = data
    def get_user(self, user_id):
        return self.store.get(user_id, {})
    def log_episode(self, user_id, episode_id, result):
        self.store.setdefault(user_id, {}).setdefault('episodes', {})[episode_id] = result
