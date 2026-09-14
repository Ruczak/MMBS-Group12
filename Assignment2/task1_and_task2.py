"""
Assignment: Metabolic Modeling (Week 2)
inspecting it, and implementing it as flux bound constraints on the E. coli core model.
"""

import cobra
import csv
from cobra.io import load_model, save_json_model

#equivalent to cobra.io.load_json_model('e_coli_core.json')

model = load_model('textbook')
#task 1
data = {}
filename = '/mnt/user-data/uploads/KEN3170_Assignment_2026_e_coli_core_expression.csv'
with open(filename, mode='r', newline='') as file: reader = csv.reader(file)
    next(reader) 
    for row in reader:
        if not row:
            continue
        
        reaction_id, value = row[0].strip(), float(row[1])
        data[reaction_id] = value

print(f"Loaded maximal activity data for {len(data)} reactions " f"(model has {len(model.reactions)} reactions total).")
     

#1a/1b
all_ids = {r.id for r in model.reactions}
missing_ids = sorted(all_ids - set(data.keys()))
print("\nReactions with NO expression data (will show as grey/no-data " "on the Escher map):")
for rid in missing_ids:
    print(" ", rid)

#task 2
original_reversibility = {r.id: r.reversibility for r in model.reactions}

for r in model.reactions:
    if r.id == 'EX_glc__D_e':
#remove the pre-existing maximal uptake bound (-10) and use the high absolute default bounds instead.
        r.lower_bound = -1000.0
        r.upper_bound = 1000.0

    elif r.id == 'ATPM':
#non-growth-associated maintenance
        pass
    elif r.id in data:
        value = data[r.id]
        if original_reversibility[r.id]:
#reversible reaction: -value / +value
            r.lower_bound = -value
            r.upper_bound = value
        else:
#irreversible reaction: 0 / +value
            r.lower_bound = 0.0
            r.upper_bound = value
#if no data available for this reaction: leave default constraints.
    else:  pass

print(f"\n{'Reaction':15s}{'Lower bound':>15s}{'Upper bound':>15s}")
for r in model.reactions:  print(f"{r.id:15s}{r.lower_bound:15.3f}{r.upper_bound:15.3f}")
save_json_model(model, 'e_coli_core_constrained.json')