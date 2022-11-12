t = int(input())
for case in range(t):
    n, k = map(int, input().split())
    lst = [list(map(int, input().split())) for i in range(n)]

    lst.sort()
    cnt = 0
    cur = 0
    for i in range(n):
        seg = lst[i]
        s, e = seg[0], seg[1]
        # alrdy covered
        if cur >= e:
            continue
        
        # start a new one
        if cur <= s:
            d = (e - s + k - 1) // k
            cnt += d
            cur = s + d * k
        # cover half way through
        else:
            d = (e - cur + k - 1) // k
            cnt += d
            cur += d * k
    print('Case #{}: {}'.format(case + 1, cnt))
