tcs = int(input())
for tc in range(tcs):
	n = int(input())
	res = n // 5
	res += 1 if n % 5 > 0 else 0
	if n <= 5:
		res = 1
	print('Case #{}: {}'.format(tc + 1, res))