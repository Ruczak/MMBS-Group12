# Epidemiological Model Assignment — Parameter Exploration

**Course**: KEN3170 — Multi-scale modeling of biological systems
**Group number**: [X]

---

## 1. Repository overview
- `analysis.ipynb` — main notebook containing all required sections (Setup, Part 1–3, Conclusions)
- `requirements.txt` — Python dependencies (numpy, matplotlib, pandas, scipy, seaborn)
- `README.md` — this file

**How to run**: `pip install -r requirements.txt` then open and run `analysis.ipynb` top to bottom (Kernel → Restart & Run All). No external data files are needed; all simulations are generated at run time.

---

## 2. Part 1 — Parameter analysis function
**Function**: `analyze_recovery_rates(beta, mu, N, I0, simulation_days)`

Solves the SIRD ODE system (`sird_model`) with `scipy.integrate.odeint` for each recovery rate in `gamma_values = [0.05, 0.1, 0.15, 0.2, 0.25]`, extracts the peak infectious count, the day it occurs, cumulative deaths, and `R0 = beta / gamma` for each run, returns them as a `pandas.DataFrame`, and plots all five infectious-curve trajectories on one figure. See the notebook for the full output table and plot.

---

## 3. Part 2 — Scenario comparison
- Result tables for Scenario A (High Transmission: `beta=0.4, mu=0.02`) and Scenario B (Low Transmission: `beta=0.2, mu=0.005`) are produced by calling `analyze_recovery_rates` with each scenario's parameters.
- A side-by-side comparative plot (one panel per scenario, same gamma values and color scale) is included.
- **Which scenario is worse for public health, and why**: Scenario A is worse at every recovery rate tested — its higher beta raises R0 and produces bigger, earlier infectious peaks, and its 4x higher mu means more deaths per infection. Full reasoning is in the notebook's Part 2 markdown discussion.

---

## 4. Part 3 — Policy recommendations
- **4.1 Parameter impact analysis** — how beta, gamma, and mu each drive epidemic size, timing, and lethality.
- **4.2 Intervention analysis** — real interventions mapped to each parameter (distancing/masking → beta, treatment/care speed → gamma, hospital capacity/triage → mu, vaccination → all three).
- **4.3 Real-world application** — how these levers should be sequenced/prioritised for high- vs low-transmission outbreaks.

---

## 5. Conclusions
Summarised in the notebook: gamma is a strong, direct lever on epidemic severity; Scenario A dominates Scenario B in harm at every tested gamma; and `R0 = beta/gamma < 1` remains the key threshold for evaluating whether a policy package will shrink an outbreak.
