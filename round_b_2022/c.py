from collections import deque

# TLE
def bfs(start, end, D):
	if start == end:
		return 0
	# [d, config]
	q = deque()
	q.append((0, start))
	seen = set()

	while q:
		d, config = q.popleft()
		if config in seen:
			continue
		seen.add(config)

		if config == end:
			return d

		for i in range(N):
			for j in range(i + 1, N):
				# update config in the range [i, j]
				lst = list(config)
				lst_1 = list(config)
				for k in range(i, j + 1):
					lst[k] = (lst[k] + 1) % D
					t = tuple(lst)
					if t == end:
						return d + 1
					if t not in seen:
						q.append((d + 1, t))
					lst_1[k] = (lst_1[k] - 1) % D
					t = tuple(lst_1)
					if t == end:
						return d + 1
					if t not in seen:
						q.append((d + 1, t))

		for i in range(N):
			lst = list(config)
			lst_1 = list(config)

			lst[i] = (lst[i] + 1) % D
			t = tuple(lst)
			if t == end:
				return d + 1
			if t not in seen:
				q.append((d + 1, t))
			lst_1[i] = (lst_1[i] - 1) % D
			t = tuple(lst_1)
			if t == end:
				return d + 1
			if t not in seen:
				q.append((d + 1, t))
	return 0
		
		

t = int(input())
for tcs in range(t):
	I = [int(n) for n in input().split()]
	dials = [int(n) for n in input().split()]
	N, D = I[0], I[1]

	start = tuple(dials)
	N = len(dials)
	end = tuple([0] * N)

	res = bfs(start, end, D)

	print('Case #{}: {}'.format(tcs + 1, res))
	
		
# 2
# 6 2
# 1 1 0 1 0 1
# 6 2
# 0 1 0 0 1 1
