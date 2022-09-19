from collections import defaultdict, deque


tcs = int(input())
for tc in range(tcs):
	N, Q = [int(n) for n in input().split()]
	adj = defaultdict(set)
	for _ in range(N - 1):
		u, v = [int(n) for n in input().split()]
		adj[u].add(v)
		adj[v].add(u)
	
	queries = []
	for _ in range(Q):
		queries.append(int(input()))
	
	# construct tree
	levels = defaultdict(int)
	levels[1] = 1
	level = 1
	root = 1
	q = deque([1])
	seen = set()
	seen.add(1)
	while q:
		n = len(q)
		cnt = 0
		for _ in range(n):
			node = q.popleft()
			for nei in adj[node]:
				if nei not in seen:
					seen.add(nei)
					q.append(nei)
					cnt += 1
		level += 1
		levels[level] = cnt

	# print(levels)

	res = 0
	for level in sorted(levels):
		require = levels[level]
		if Q >= require:
			res += require
			Q -= require
		else:
			break
	

	print('Case #{}: {}'.format(tc + 1, res))


