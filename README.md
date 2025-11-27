# Digital Twin AI  (Gemini Integrated)

A complete multi-agent simulation environment for:
- Creating a personal Digital Twin
- Running scenario-based weekly simulations
- Multi-objective optimization (Pareto front)
- Agent-based planning + Gemini explanations
- Tools, memory, sessions, observability, A2A routing
- Suitable for Kaggle, Google Colab, or local Jupyter

## Features
✔ Multi-agent architecture  
✔ Sequential, parallel, and loop agents  
✔ LLM agent powered by Google Gemini  
✔ Tools (Echo, safe Python executor)  
✔ Persistent MemoryBank  
✔ InMemorySessionService  
✔ Agent-to-Agent Router (A2A)  
✔ Observability (logging + metrics)  
✔ Synthetic user evaluation pipeline  
✔ Ready-to-run Kaggle notebook  

## Structure
src/
twin.py
scenario_gen.py
simulator.py
evaluator.py
memory_bank.py
session_service.py
tools.py
agent_core.py
gemini_agent.py
a2a_router.py
observability.py


## Requirements
Install via:
pip install -r requirements.txt

python
Copy code

## Using Gemini
Set your API key:
```python
import os
os.environ["GEMINI_API_KEY"] = ""
