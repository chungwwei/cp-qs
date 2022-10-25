from itertools import groupby
t = int(input())
for tcs in range(t):
    n = int(input())
    s = [int(n) for n in input()]

    i = 0
    j = n - 1
    while i < n and s[i] != 1:
        i += 1

    while j >= 0 and s[j] != 1:
        j -= 1
    
    res = 0
    k = 0
    while k < i:
        res += abs(i - k)
        k += 1

    k = n - 1
    while k > j:
        res += abs(j - k)
        k -= 1
    
    A = s[i: j + 1]
    for v, grp in groupby(A):
        if v == 1:
            continue
        length = len(list(grp))

        if length % 2 == 0:
            for m in range(1, length // 2 + 1):
                res += m * 2
        else:
            for m in range(1, length // 2 + 2):
                if m == length // 2 + 1:
                    res += m
                else:
                    res += m * 2

    print('Case #{}: {}'.format(tcs + 1, res))