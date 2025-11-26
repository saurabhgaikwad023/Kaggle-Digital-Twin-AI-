class MemoryBank:
    def __init__(self):
        self.store={}
    def save_user(self,user,data):
        self.store[user]=data
    def get_user(self,user):
        return self.store.get(user,{})
    def log_episode(self,user,episode,res):
        self.store.setdefault(user,{}).setdefault("episodes",{})[episode]=res
