from queue import Queue, Empty

class A2ARouter:
    def __init__(self):
        self.queues = {}
    def register(self, agent_id:str):
        self.queues[agent_id] = Queue()
    def send(self, to_agent:str, msg:dict):
        q = self.queues.get(to_agent)
        if q: q.put(msg)
    def recv(self, agent_id:str, timeout:float=0.1):
        try:
            return self.queues[agent_id].get(timeout=timeout)
        except Empty:
            return None
