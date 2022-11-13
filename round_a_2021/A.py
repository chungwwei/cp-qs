t = int(input())
for tcs in range(t):
    n, k = [int(n) for n in input().split()]
    s = [n for n in input()]

    cnt = 0
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            cnt += 1
    
    mx = max(0, abs(k - cnt))
    print('Case #{}: {}'.format(tcs + 1, mx))
