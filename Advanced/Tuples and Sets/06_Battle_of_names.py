n = int(input())

odd_set = set()
even_set = set()

for num in range(1, n + 1):
    name = input()
    sum_chr = 0
    for chr in name:
        sum_chr += ord(chr)
    result = sum_chr // num
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)


if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(even_set) > sum(odd_set):
    print(*even_set.symmetric_difference(odd_set), sep=", ")