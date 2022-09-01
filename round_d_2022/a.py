tcs = int(input())
for tc in range(tcs):
	N, M = [int(n) for n in input().split()]
	A = [int(n) for n in input().split()]

	A.sort()
	j = N - 1
	res = 0
	while j > -1 and M > 1:
		res += A[j]
		M -= 1
		j -= 1
	
	# find the median in rest
	rest = A[: j + 1]
	n = len(rest)
	median = 0
	# even
	if n % 2 == 0:
		median = (rest[n // 2] + rest[n // 2 - 1]) / 2
	else:
		median = rest[n // 2]

	res += median
	print('Case #{}: {}'.format(tc + 1, res))