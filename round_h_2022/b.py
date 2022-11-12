def dfs(basket, mark, ratio, L, memo):
	if (basket, mark, ratio) in memo:
		return memo[(basket, mark, ratio)]
	if basket == L:
		return 0
	if basket > L:
		return float("inf")

	mn = float('inf')
	if mark:
		if basket + 1 <= L:
			a = dfs(basket + 1, mark, ratio, L, memo) + 1
			mn = min(mn, a)
		if basket + ratio <= L:
			a = dfs(basket + ratio, mark, ratio, L, memo) + 2
			mn = min(mn, a)
	else:
		if basket + 1 <= L:
			a = dfs(basket + 1, mark, ratio, L, memo) + 1
			mn = min(mn, a)
		if basket > 1:
			a = dfs(basket, True, basket, L, memo) + 4
			mn = min(mn, a)
	
	memo[(basket, mark, ratio)] = mn
	return mn

tcs = int(input())
for tc in range(tcs):
	L = int(input())
	res = dfs(0, False, 0, L, {})
	print('Case #{}: {}'.format(tc + 1, res))

