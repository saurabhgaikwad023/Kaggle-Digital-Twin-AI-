import logging, time
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('digital_twin')

class Metrics:
    def __init__(self):
        self.m = {}
    def inc(self,k,v=1): self.m[k]=self.m.get(k,0)+v
    def set(self,k,v): self.m[k]=v
    def export(self): return dict(self.m)

metrics = Metrics()
