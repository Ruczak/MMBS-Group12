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

### Mutation B: MYC Amplification

We set the rule for MYC expression as ALWAYS ON. The same as in the mutation A, a stressed cell keeps growing after the mutation.

The results are the same as in the mutation A case, we have two attractor states: both with cell growth without death, and the cancerous one causes DNA damage and the other not. As we can also see, the p53, p21 are off, and MYC is on, which make CDK2 overactive, just like in the mutation A (p53 off).

From output of the rules, we can see that MYC. p21 and p53 are directly connected through the rules, which directly affect CDK2:

```markdown
p21 = p53
CDK2 = MYC AND (NOT p21) AND (NOT p53)
MDM2 = MYC = 1
p53 = DNA_damage AND (NOT MDM2)
```

Thus, `p21 = p53` become both 0, since `MYC = MDM2` is always 1, which then causes `NOT MDM2` conditions to always be false. This feedback loop causes two stable steady-states, one with DNA damage, the other not.

### Mutation C: MDM2 overexpression

MDM2 is set to always ON. MDM2 blocks p53 so p53 never turns on even with DNA damage.

The stressed cell keeps growing instead of dying, the other two scenarios are the same as normal.

Cancer-like states go from 8/256 (3.125%) to 128/256 (50%) and there are only 2 attractors because the death one is gone.

This is the same as Mutation A since MDM2 is the only thing turning p53 off in the rules, so MDM2 always on works out the same as p53 always off. The stressed cell just takes a few more steps to settle (7 instead of 4) because p53 turns on for one step before MDM2 blocks it.

### Mutation D: apoptosis evasion (Death suppressed)

We switch Death OFF permanently. All three scenarios stay the same as normal, except the stressed cell no longer dies — it now arrests instead.

Of 256 starting states, cancer-like growth stays at 8 (3.125%), same as normal.

The 120 states that used to lead to death now settle into a new arrested state instead (p53 ON, p21 ON, Growth OFF, Death OFF).

Mutation D has three fixed attractors, same as the normal network.

p53 still shuts down CDK2 and MYC when DNA damage is present, so Growth stays blocked.

Losing Death alone removes the ability to die, but not the brake on growth — so cells get stuck instead of turning cancerous.

## Limitations

1. All nodes update together, while real cell processes take different amounts of time.
2. We only analyse an important, but limited part of interactions affecting the growth of this concrete cancer.
3. Every node is just on or off. In a real cell things like p53 or MYC have levels, so a bit of p53 would still slow growth down a little instead of doing nothing at all until it is fully on.

## Conclusions

Mutations A, B let damaged cells keep growing, because of the feedback loop they share.

CDK2, p53, MYC and DNA damage are directly connected to the growth and death of the cells. That is why affecting at least one of these nodes in the network can change the steady state towards the cancerous growth.

```markdown
Growth = CDK2 AND MYC AND (NOT p53)
Death = p53 AND DNA_damage AND (NOT Growth)
```
