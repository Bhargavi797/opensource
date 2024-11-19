n = int(input())
arr = map(int, input().split())
absent = 0
c = 0
for i in arr:
    if i == 0:
        c += 1
        absent = max(absent, c)
    else:
        c =0
print(absent)
        
    
