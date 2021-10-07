from collections import deque

bees = deque([int(i) for i in input().split()])
nectar = [int(i) for i in input().split()]
symbols = deque(input().split())

honey = 0

while bees:

    if nectar:
        if nectar[-1] >= bees[0]:
            if symbols[0] == "+":
                honey += abs(bees[0] + nectar[-1])
            elif symbols[0] == "-":
                honey += abs(bees[0] - nectar[-1])
            elif symbols[0] == "*":
                honey += abs(bees[0] * nectar[-1])
            elif symbols[0] == "/":
                if bees[0] > 0 and nectar[-1] > 0:
                    honey += abs(bees[0] / nectar[-1])
            nectar.pop()
            bees.popleft()
            symbols.popleft()

        else:
            nectar.pop()
    else:
        break


print(f"Total honey made: {honey}")
if bees:
    bees = [str(i) for i in bees]
    print(f"Bees left: {', '.join(bees)}")
if nectar:
    nectar = [str(i) for i in nectar]
    print(f"Nectar left: {', '.join(nectar)}")