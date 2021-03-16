for _ in range(int(input())):
    q,d = map(int, input().split())
    A = list(map(int, input().split()))
    for a in A:
        while a>0:
            if str(d) in str(a):
                print("YES")
                break
            else:
                a=a-d
        else:
            print("NO")