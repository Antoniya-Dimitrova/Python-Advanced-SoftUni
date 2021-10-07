n = int(input())

unique_compounds = set()

for _ in range(n):
    chemical_compounds = input().split()
    for el in chemical_compounds:
        unique_compounds.add(el)

[print(j) for j in unique_compounds]