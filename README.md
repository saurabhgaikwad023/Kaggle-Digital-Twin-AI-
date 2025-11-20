Digital Twin Simulator — Freestyle Capstone Project (Kaggle x Google),
This repository contains the complete implementation of the Digital Twin Simulator, 
a Freestyle Track submission for the Kaggle 5-Day AI Agents Intensive Capstone.

The system builds a lightweight digital twin of a user, generates dozens of 
weekly life scenarios, simulates outcomes (productivity, stress, commute, cost, social 
balance), evaluates multi-objective tradeoffs, and recommends Pareto-efficient weekly plans.

No API keys are used. All external APIs are mocked with safe stubs.

---

:star:
Click to learn more
 Features,
Lightweight human behavioral digital twin model,
Multi-agent system:
TwinBuilderAgent,
ScenarioGeneratorAgent,
SimulationAgents,
OutcomeEvaluatorAgent,
PlanChooserAgent,
MemoryBank,
,
Exhaustive scenario generation (40–100 per run),
Simulation-driven decision making,
Pareto front multi-objective optimization,
Explainable recommendations (Mock LLM used),
Synthetic user evaluation across 50 users,
Fully reproducible with no external dependencies,

---

:brain:
Click to learn more
 Project Structure,
:joy:
Click to react
:heart:
Click to react
:hearts:
Click to react
Add Reaction
Edit
Forward
More

xoxo.Damo

ENG
 — 01:36Thursday, 20 November, 2025 01:36
agents/ → modular AI agent modules
notebook/ → Kaggle-friendly notebook
docs/ → Word documents for submission
assets/ → diagrams, thumbnails
[01:38]Thursday, 20 November, 2025 01:38
---

:jigsaw:
Click to learn more
 Agents Overview,
twin_builder.py: Generates the digital twin,
scenario_gen.py: Creates weekly plan variations,
simulator.py: Runs simulations for each scenario,
evaluator.py: Scoring + Pareto frontier logic,
memory.py: Long-term user preference store,
llm_wrapper.py: Stub for LLM explanations (replace with Gemini if needed),

---

:bar_chart:
Click to learn more
 Evaluation,
We simulate 50 synthetic users to measure:
Productivity gain,
Stress reduction,
Commute reduction,
Social balance shifts,
Cost savings,

Visualization included:
Productivity histogram,
Stress distribution,
Pareto front heatmaps,

---

:tools:
Click to learn more
 Running the Notebook,
Open digital_twin_simulator.ipynb in Kaggle or Jupyter,
Run cells top-to-bottom,
Replace MockLLM with Gemini for bonus points (optional),
Results appear at the bottom (plots + tables),

---

:closed_lock_with_key:
Click to learn more
 Security Notes,
No API keys used in this repo,
All real-world integrations must use environment variables,
Never commit secrets,
Production deployments require encrypted storage,
