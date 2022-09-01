res = []
def dfs(i, arr, n, amount, total, X, Y, path):

	if amount > 0 and total - amount > 0 and Y > 0 and amount / (total - amount) == X / Y:
		global res 
		res = path[:]
		return True

	if i >= n:
		return False
	
	# take	
	path.append(arr[i])
	a = dfs(i + 1, arr, n, amount + arr[i], total, X, Y, path)
	if path:
		path.pop()
	# skip
	b = dfs(i + 1, arr, n, amount, total, X, Y, path)
	return a or b


tcs = int(input())
for tc in range(tcs):
	A = [int(n) for n in input().split()]
	N, X, Y = A[0], A[1], A[2]

	B = [n for n in range(1, N + 1)]
	n = len(B)
	total = (n + 1) * n / 2

	dfs(0, B, n, 0, total, X, Y, [])
	if not res or len(res) == 0:
		print('Case #{}: {}'.format(tc + 1, "IMPOSSIBLE"))
	else:
		res = [str(n) for n in res]
		print('Case #{}: {}'.format(tc + 1, "POSSIBLE"))
		print(len(res))
		print(' '.join(res))