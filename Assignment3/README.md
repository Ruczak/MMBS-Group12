# Network modelling

**Course**: KEN3170 — Multi-scale modeling of biological systems
**Group number**: 12

## Repository overview

- `assignment3.ipynb` — main notebook containing all required sections
- `requirements.txt` — Python dependencies for the network simulations and plots
- `README.md` — this file

**How to run**: `pip install -r requirements.txt` then open and run `.ipynb` top to bottom (Kernel → Restart & Run All). No external data files are needed; all simulations are generated at run time.

## Exercises

### Mutation A: p53 knockout

We switch p53 OFF. The stressed cell keeps growing despite DNA damage. The other two scenarios stay the same.

Of 256 starting states, cancer-like growth rises from 8 (3.125%) to 128 (50%). This means growth with DNA damage and no death. Mutation A has two fixed attractors; the normal network has three.

MYC activates MDM2, which blocks p53. Since p53 blocks MYC, this loop can keep growth active. Losing p53 removes a brake on growth.

## Limitations

1. All nodes update together, while real cell processes take different amounts of time.

## Conclusions

Mutation A lets damaged cells keep growing.
