def solve(i1, j1, i2, j2, k, A, B, m, n):
	def dfs(i1, j1, i2, j2, k):
		if k <= 0:
			return 0
		if i1 > j1:
			return 0
		if i2 > j2:
			return 0
		
		ans = 0
		if i1 + 1 < m:
			ans = max(ans, dfs(i1 + 1, j1, i2, j2, k - 1) + A[i1])
		if j1 - 1 >= 0:
			ans = max(ans, dfs(i1, j1 - 1, i2, j2, k - 1) + A[j1])
		if i2 + 1 < n:
			ans = max(ans, dfs(i1, j1, i2 + 1, j2, k - 1) + B[i2])
		if j2 - 1 >= 0:
			ans = max(ans, dfs(i1, j1, i2, j2 - 1, k - 1) + B[j2])
		# ans = max(ans, a)
		# ans = max(ans, b)
		# ans = max(ans, c)
		# ans = max(ans, d)
		return ans

	return dfs(i1, j1, i2, j2, k)

tcs = int(input())
for tc in range(tcs):
	m = int(input())
	A = [int(n) for n in input().split()]
	n = int(input())
	B = [int(n) for n in input().split()]
	k = int(input())

	res = solve(0, m - 1, 0, n - 1, k, A, B, m, n)

	print('Case #{}: {}'.format(tc + 1, res))


