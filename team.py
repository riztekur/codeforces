#https://codeforces.com/problemset/problem/231/A

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

solved = 0
for a in arr:
    if sum(a) > 1:
        solved = solved  + 1

print(solved)