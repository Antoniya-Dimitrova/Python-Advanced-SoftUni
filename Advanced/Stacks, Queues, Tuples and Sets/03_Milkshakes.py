from collections import deque

chocolates = [int(i) for i in input().split(", ")]
cups_of_milk = deque([int(j) for j in input().split(", ")])

count = 0

while not count == 5:
    if not chocolates or not cups_of_milk:
        break

    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.pop()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    if chocolates[-1] == cups_of_milk[0]:
        count += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates[-1] -= 5

if count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    chocolates = [str(i) for i in chocolates]
    print(f"Chocolate: {', '.join(chocolates)}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    cups_of_milk = [str(i) for i in cups_of_milk]
    print(f"Milk: {', '.join(cups_of_milk)}")
else:
    print("Milk: empty")