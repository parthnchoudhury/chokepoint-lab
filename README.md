# ⛓️ chokepoint-lab 
**Geopolitical Disruption Simulator for Supply Chain Contingency Planning**

> A tactical modeling and forecasting toolkit for high-risk trade corridors — starting with the Strait of Hormuz.

## 🌍 Overview

**`chokepoint-watch`** is an open-source Python toolkit designed to simulate, analyze, and visualize the impact of geopolitical disruptions—like the closure of the Strait of Hormuz—on global supply chains, trade flows, and critical commodity access.

It was developed to support the analysis published in our **Substack premium edition** on the 2025 Iran–Israel conflict and its cascading impact on oil & LNG trade, particularly through the world’s most sensitive trade chokepoints.

## 🚀 Use Cases

- Simulate trade disruptions across maritime chokepoints
- Analyze impact on oil/LNG flows to regions like EU, China, India
- Visualize alternative routing and delivery delays
- Run Monte Carlo simulations for resilience planning
- Generate supply chain Impact x Feasibility matrices
- Model demand destruction for exposed nations (e.g., Pakistan, Bangladesh)

## 📦 Features

### 🔁 Monte Carlo Simulation Engine
Predict route delays, volume losses, and commodity price effects based on historical, stochastic, or custom parameters.

### 📊 Feasibility x Impact Matrix Generator
Assess strategies across disruption stages — from rerouting to rationing to partner re-alignment.

### 🗺️ Global Trade Network Mapper
Route modeling with support for chokepoint tagging (Strait of Hormuz, Suez Canal, Bosphorus, Taiwan Strait).

### 🧠 AI-Enabled Sentiment & Risk Parser
Use NLP to ingest geopolitical news and forecast probable escalation levels based on language and source weight.

## 🧰 Technologies Used

- Python 3.11+
- Pandas / NumPy / SciPy
- NetworkX
- Plotly / Dash
- Natural Language Toolkit (NLTK) / HuggingFace Transformers
- Flask (for browser-based reporting suite)
- Docker (optional deployment)
- [supplychainpy](https://github.com/dtgroup/chokepoint-lab) integration for EOQ, demand planning, and safety stock modeling

## 🛠️ Quick Start

### 🔨 Clone & Install

```bash
git clone https://github.com/your-org/chokepoint-lab.git
cd chokepoint-lab
pip install -r requirements.txt

### Run Simulation

```bash
python simulate.py --scenario hormuz_closure --region EU --output ./results/
```

### Launch Report Dashboard

```bash
chokepoint-lab data.csv -a -loc ./results -l
```
Then visit http://localhost:5000 in your browser.

### Project Structure

### Premium Features (Substack Subscribers Only)

	•	🔄 Route rerouting optimizer for Hormuz → Cape of Good Hope switch
	•	🧠 Integrated LLM-based risk summary (GPT / Claude)
	•	📊 Exportable Feasibility Matrix (PDF, CSV, HTML)
	•	📈 Visual trade risk scoring by commodity & region
	•	🎓 Python Notebooks for scenario training & modification

 ### Example Scenarios

```bash
 # Strait of Hormuz full closure
python simulate.py --scenario hormuz_blockade --duration 14 --region Asia

# Israel refinery shutdown ripple effect
python simulate.py --scenario israel_refinery_outage --region MENA

# Combined chokepoint impact: Hormuz + Red Sea
python simulate.py --scenario double_blockade --region Global
```

### Contribution

We welcome community input to expand this repository with new chokepoint datasets (Suez, Panama, Taiwan), regional demand models, or trade policy simulators.
	1.	Fork this repo
	2.	Create a feature branch
	3.	Submit a pull request

### License

This repository is licensed under Apache 2.0. For commercial or enterprise usage, please contact us directly.


