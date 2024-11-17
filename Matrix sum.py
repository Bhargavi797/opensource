n = int(input())
mx = []
for _ in range(n):
    mx.append(list(map(int, input().split())))
re = []
for i in range(n):
    row = sum(mx[i])
    col = sum(mx[j][i] for j in range(n))
    re.append(row+col) 
print(*re)
    
