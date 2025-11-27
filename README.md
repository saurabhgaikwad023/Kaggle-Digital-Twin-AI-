# Digital Twin AI (Multi-Agent + Gemini optional)

This repository contains the Digital Twin multi-agent system (notebook code converted into modular files).

**Features**
- Twin dataclass, scenario generator, simulator
- Evaluator (Pareto front, scoring)
- MemoryBank (persistent), InMemorySessionService
- Tools (Echo, safe Python exec)
- Agent core (AgentManager) + GeminiAgent (optional)
- Agent-to-Agent router (A2A)
- Observability (metrics)
- Plotting cells available in the notebook

**Usage**
1. Install dependencies: `pip install -r requirements.txt`
2. (Optional) Set Gemini API key at runtime:
```py
import os
os.environ['GEMINI_API_KEY'] = 'YOUR_KEY'
