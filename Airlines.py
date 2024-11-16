x, n = map(int, input().split())
total = x*100
if total >= n:
    planes = 0
else:
    balance_planes = n-total
    planes = (balance_planes + 99) // 100
print(planes)
