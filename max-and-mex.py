# https://codeforces.com/problemset/problem/1496/B

import math
 
def mex(S):
    i=0
    while i in S:
        i+=1
    return i
 
for _ in range(int(input())):
    n,k = map(int,input().split())
    s = set(map(int,input().split()))
    a = mex(s)
    b = max(s)

    if a==len(s):
        print(n+k)
    else:
        if k>0:
            s.add(int(math.ceil((a+b)/2)))
        print(len(s))