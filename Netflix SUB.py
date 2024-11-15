A, B, C, X = list(map(int, input().split()))
if (A+B or B+C or C+A) >= X:
    print("YES")
else:
    print("NO")
