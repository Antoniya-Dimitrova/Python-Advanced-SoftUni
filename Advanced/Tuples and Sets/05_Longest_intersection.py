n = int(input())

intersection = set()

for _ in range(n):
    first_set = set()
    second_set = set()
    first_range, second_range = input().split("-")
    first_start, first_end = first_range.split(',')
    first_start = int(first_start)
    first_end = int(first_end)
    second_start, second_end = second_range.split(',')
    second_start = int(second_start)
    second_end = int(second_end)

    for i in range(first_start, first_end + 1):
        first_set.add(i)
    for j in range(second_start, second_end + 1):
        second_set.add(j)

    if len(first_set.intersection(second_set)) > len(intersection):
        intersection = first_set.intersection(second_set)
print(f"Longest intersection is {list(intersection)} with length {len(intersection)}")