x, y, z = list(map(int, input().split()))
total = x*y
available = z*1440
if total <= available:
    print("YES")
else:
    print("NO")
