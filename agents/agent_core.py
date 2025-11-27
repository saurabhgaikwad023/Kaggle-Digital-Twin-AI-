import threading, time, json
import logging
logger = logging.getLogger('digital_twin')
logging_level = logging.INFO
logging.basicConfig(level=logging_level, format='%(asctime)s %(levelname)s %(message)s')

class Agent:
    def __init__(self, id:str, tools:dict=None):
        self.id = id
        self.tools = tools or {}
    def act(self, ctx:dict) -> dict:
        return {'agent': self.id, 'status': 'noop'}

class AgentManager:
    def __init__(self):
        self.agents = {}
    def register(self, agent:Agent):
        self.agents[agent.id] = agent
    def run_sequential(self, order:list, ctx:dict):
        for aid in order:
            a = self.agents[aid]
            logger.info(f'Running agent {aid} sequentially')
            out = a.act(ctx)
            ctx.update(out)
        return ctx
    def run_parallel(self, ids:list, ctx:dict, timeout:float=10.0):
        threads=[]; results=[]
        def run_agent(aid):
            results.append(self.agents[aid].act(ctx.copy()))
        for aid in ids:
            t = threading.Thread(target=run_agent, args=(aid,))
            t.start(); threads.append(t)
        for t in threads: t.join(timeout)
        for r in results: ctx.update(r)
        return ctx
    def run_loop(self, aid:str, ctx:dict, iterations:int=3, sleep:float=0.1):
        for _ in range(iterations): out = self.agents[aid].act(ctx); ctx.update(out); time.sleep(sleep)
        return ctx
