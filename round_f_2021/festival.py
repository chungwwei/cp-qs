from collections import defaultdict
t = int(input())
for tcs in range(t):
	D, N, K = [int(n) for n in input().split()]
	intervals = []
	delta = defaultdict(int)
	limit = defaultdict(set)
	for i in range(N):
		happiness, s, e = [int(n) for n in input().split()]
		intervals.append((s, e, happiness))

		if len(limit[s]) < K:
			limit[s].add((s, e, happiness))
			delta[s] += happiness
		if len(limit[e]) < K:
			limit[e].add((s, e, happiness))
			delta[e] += happiness
		

	# intervals.sort(key=lambda x: -x[2])
	# for s, e, happiness in intervals:
	# 	delta[s] += happiness
	# 	delta[e + 1] -= happiness

	res = 0
	for event in delta:
		res = max(res, delta[event])
	print('Case #{}: {}'.format(tcs + 1, res))