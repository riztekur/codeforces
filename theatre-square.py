from math import ceil

n,m,a=map(int, input().split())
result = ceil(m/a) * ceil(n/a)
print(result)