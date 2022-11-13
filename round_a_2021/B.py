def tally(a, b):
    cnt = 0
    while a >= 2:
        if a * 2 <= b:
            cnt += 1
        a -= 1
    return cnt

def cnt(i, j, R, C, A):
    total = 0
    L = [(i, j + 1, 'up', i + 1, j, 'right'), (i, j + 1, 'up', i - 1, j, 'left'), (i + 1, j, 'right', i, j - 1, 'down'), (i - 1, j, 'left', i, j - 1, 'down')]
    for ni, nj, d1, nr, nc, d2 in L:
        if 0 <= ni < R and 0 <= nj < C and 0 <= nr < R and 0 <= nc < C:
            a, b = 1, 1
            if A[ni][nj] == 1 and A[nr][nc] == 1:
                a = dfs(i, j, d1, R, C, A)
                b = dfs(i, j, d2, R, C, A)
                c, d = tally(a, b), tally(b, a)
                total += c + d

    return total

def dfs(i, j, dir, R, C, A):
    if 0 <= i < R and 0 <= j < C and A[i][j] == 1:
        if dir == 'right':
            return 1 + dfs(i + 1, j, dir, R, C, A)
        elif dir == 'left':
            return 1 + dfs(i - 1, j, dir, R, C, A)
        elif dir == 'up':
            return 1 + dfs(i, j + 1, dir, R, C, A)
        elif dir == 'down':
            return 1 + dfs(i, j - 1, dir, R, C, A)
    return 0




t = int(input())
for tcs in range(t):
    R, C = [int(n) for n in input().split()]
    A = []
    for i in range(R):
        A.append([int(n) for n in input().split()])

    res = 0
    for i in range(R):
        for j in range(C):
            if A[i][j] == 1:
                res += cnt(i, j, R, C, A)
    
    print('Case #{}: {}'.format(tcs + 1, res))