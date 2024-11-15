t = int(input())
for i in range(0, t):
    n, m = list(map(int, input().split()))
    re = n-m
    if re>0:
        print(re)
    else:
        print(0)
