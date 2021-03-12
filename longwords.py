# https://codeforces.com/problemset/problem/71/A

n = int(input())

words = []
for i in range(n):
    words.append(input())

for word in words:
    if len(word) <= 10:
        print(word)
    else:
        print(word[0] + str(len(word)-2) + word[-1])