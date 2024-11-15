n = int(input())
ele = [list(map(int, input().split())) for _ in range(n)]
for line in ele:
    print(*line[::-1])
