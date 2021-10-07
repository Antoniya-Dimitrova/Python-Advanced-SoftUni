from collections import deque

materials = [int(i) for i in input().split()]
magic_level = deque([int(i) for i in input().split()])

presents = {"Doll": int(0), "Wooden train": int(0), "Teddy bear": int(0), "Bicycle": int(0)}

while True:
    if not materials or not magic_level:
        break
    if materials[-1] * magic_level[0] == 150:
        presents["Doll"] += 1
        materials.pop()
        magic_level.popleft()
    elif materials[-1] * magic_level[0] == 250:
        presents["Wooden train"] += 1
        materials.pop()
        magic_level.popleft()
    elif materials[-1] * magic_level[0] == 300:
        presents["Teddy bear"] += 1
        materials.pop()
        magic_level.popleft()
    elif materials[-1] * magic_level[0] == 400:
        presents["Bicycle"] += 1
        materials.pop()
        magic_level.popleft()
    else:
        if materials[-1] == 0 and magic_level[0] == 0:
            materials.pop()
            magic_level.popleft()
            continue
        if materials[-1] == 0:
            materials.pop()
            continue
        if magic_level[0] == 0:
            magic_level.popleft()
            continue
        if materials[-1] * magic_level[0] < 0:
            materials.append(magic_level.popleft() + materials.pop())
            continue
        if materials[-1] * magic_level[0] > 0:
            magic_level.popleft()
            materials[-1] += 15
            continue
if presents["Doll"] > 0 and presents["Wooden train"] > 0:
    print("The presents are crafted! Merry Christmas!")
elif presents["Teddy bear"] > 0 and presents["Bicycle"] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    materials.reverse()
    print("Materials left: ", end="")
    print(*materials, sep=", ")
if magic_level:
    print("Magic left: ", end="")
    print(*magic_level, sep=", ")

presents_sorted = sorted(presents.items(), key=lambda x: x[0])

for key, value in presents_sorted:
    if value > 0:
        print(f"{key}: {value}")