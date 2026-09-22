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


## Mutation D: apoptosis evasion (Death suppressed)

We switch Death OFF permanently. All three scenarios stay the same as normal, except the stressed cell no longer dies — it now arrests instead.

Of 256 starting states, cancer-like growth stays at 8 (3.125%), same as normal. 

The 120 states that used to lead to death now settle into a new arrested state instead (p53 ON, p21 ON, Growth OFF, Death OFF).

Mutation D has three fixed attractors, same as the normal network.

p53 still shuts down CDK2 and MYC when DNA damage is present, so Growth stays blocked. 

Losing Death alone removes the ability to die, but not the brake on growth — so cells get stuck instead of turning cancerous.

## Limitations

1. All nodes update together, while real cell processes take different amounts of time.

## Conclusions

Mutation A lets damaged cells keep growing.
