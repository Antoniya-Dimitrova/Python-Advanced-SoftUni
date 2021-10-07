first_set = set([int(k) for k in input().split()])
second_set = set([int(l) for l in input().split()])

n = int(input())

for _ in range(n):

    task = input().split()

    if task[0] == "Add":
        if task[1] == "First":
            for i in range(2, len(task)):
                first_set.add(int(task[i]))
        elif task[1] == "Second":
            for j in range(2, len(task)):
                second_set.add(int(task[j]))

    elif task[0] == "Remove":
        if task[1] == "First":
            for m in range(2, len(task)):
                first_set.discard(int(task[m]))
        elif task[1] == "Second":
            for n in range(2, len(task)):
                second_set.discard(int(task[n]))

    elif task[0] == "Check" and task[1] == "Subset":
        if first_set.issubset(second_set) or first_set.issuperset(second_set):
            print(True)
        else:
            print(False)

first_set_sorted = sorted(first_set)
second_set_sorted = sorted(second_set)

print(*first_set_sorted, sep=", ")
print(*second_set_sorted, sep=", ")