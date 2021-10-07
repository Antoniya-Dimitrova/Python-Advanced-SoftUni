n, m = input().split()
n = int(n)
m = int(m)

n_set = set()
m_set = set()

for i in range(n):
    n_nums = input()
    n_set.add(n_nums)

for j in range(m):
    m_nums = input()
    m_set.add(m_nums)

print('\n'.join(n_set.intersection(m_set)))
