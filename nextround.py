# https://codeforces.com/problemset/problem/158/A

m,n=map(int,input().split())
arr=list(map(int,input().split()))
print(len([x for x in arr if x >= arr[n-1] and x > 0]))