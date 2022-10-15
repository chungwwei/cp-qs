tcs = int(input())
for tc in range(tcs):
	N = int(input())
	arr = [int(n) for n in input().split()]

	P = [0] * (N + 1)
	for i in range(1, len(P)):
		P[i] = P[i - 1] + arr[i - 1]
	# print(f"prefix is: {P}")

	res = 0
	for i in range(N + 1):
		for j in range(i + 1, N + 1):
			# print((i, j, P[j] - P[i]))
			if P[j] - P[i] < 0:
				break
			res += P[j] - P[i]



	print('Case #{}: {}'.format(tc + 1, res))