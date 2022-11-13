from collections import deque
t = int(input())
for tcs in range(t):
    R, C = [int(n) for n in input().split()]
    grid = []
    for i in range(R):
        grid.append([int(n) for n in input().split()])

    res = 0
    order = sorted([[r,c] for r in range(R) for c in range(C)], key=lambda l: grid[l[0]][l[1]], reverse=True)

    for r0,c0 in order:
        bfs = deque([[r0,c0]])

        while bfs:
            r,c = bfs.popleft()
            
            for nr,nc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if 0<=nr<R and 0<=nc<C and grid[r][c]-1 > grid[nr][nc]:
                    res += grid[r][c]-1-grid[nr][nc]
                    grid[nr][nc] = grid[r][c]-1
                    bfs.append([nr,nc])
        
    print(f"Case #{tcs+1}: {res}")



