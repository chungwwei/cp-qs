def solve(A, n, x):
    K = [0] * n
    for i in range(n):
        q = A[i] // x
        q += 1 if A[i] % x > 0 else 0
        K[i] = [i ,q]

    K = sorted(K, key=lambda x: (x[1], x[0]))
    res = []
    for i, q in K:
        res.append(str(i + 1))
    return ' '.join(res)
    

t = int(input())
k = t
res = []
while t:
    line = [int(n) for n in input().split()]
    n = line[0]
    x = line[1]
    A = [int(n) for n in input().split()]
    ans = solve(A, n, x)
    string = 'Case #{}: {}'.format(k - t + 1 , ans)
    res.append(string)
    t -= 1

for r in res:
    print(r)