n = int(input())
arr = map(int, input().split())
re = 0
for i in arr:
    re ^= i
print(re)
    
