# Metabollic modeling in COBRApy

**Course**: KEN3170 — Multi-scale modeling of biological systems
**Group number**: 12

## Repository overview

- `modelling.ipynb` — main notebook containing all required sections
- `requirements.txt` — Python dependencies (cobra, escher, pandas, matplotlib, numpy, ipykernel)
- `README.md` — this file

**How to run**: `pip install -r requirements.txt` then open and run `.ipynb` top to bottom (Kernel → Restart & Run All). No external data files are needed; all simulations are generated at run time.

## Exercises

### Part 1

TODO!!

### Part 2 - Implementation of maximal reaction activity data

All instructions were implemented inside a single `for`-loop. Flux boundaries of both reversible and irreversbile reactions were set according to the `KEN3170_Assignment_2026_e_coli_core_expression` file. Reactions with no data available file were skipped. Exceptions (_ATPM_ and _glucose exchange reaction_) were handled at the beginning of each iteration.

The transformed data was displayed using `pandas` library.

### Part 3

TODO!!

### Part 4

The glucose uptake bound was increased from 1 to 15 mmol/gDW/h in steps of 0.1 inside a `while`-loop, running FBA at each step and plotting the growth rate with `matplotlib`. The stored solutions were then used to check which reactions hit their activity bounds and which exchange fluxes change between the segments of the curve.

## Conclusions

Put your conclusions here
