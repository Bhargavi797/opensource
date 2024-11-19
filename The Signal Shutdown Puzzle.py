def f_g(grid, n, m):
    rows = set()
    cols = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(n):
        for j in range(m):
            if i in rows or j in cols:
                grid[i][j] = 0
    return grid
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
re_gr = f_g(grid, n, m)
for row in re_gr:
    print(' '.join(map(str, row)))
