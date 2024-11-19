n = int(input())
mtrx = []
for _ in range(n):
    mtrx.append(list(map(int, input().split())))
transpose = [[mtrx[j][i] for j in range(n)] for i in range(n)]
for row in transpose:
            print(*row)
