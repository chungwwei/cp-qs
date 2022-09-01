from collections import defaultdict
from collections import deque

def solve(n, S, m, K):
	mp = defaultdict(set)
	for index, key in enumerate(K):
		mp[key].add(index)
	
	mn = float('inf')
	# <key_index, string_index ,time>
	q = deque()
	q.append((0, 0, 0))
	while q:
		k_index, s_index, time = q.popleft()
		if s_index == n - 1:
			time = min(time, mn)
		for jump in mp[S[s_index]]:
			q.append(jump, s_index + 1, abs(k_index - jump))

	



tcs = int(input())
for tc in range(tcs):
	n = int(input())
	S = [int(n) for n in input().split()]
	m = int(input())
	K = [int(n) for n in input().split()]

	res = solve(n, S, m, K)

	print('Case #{}: {}'.format(tc + 1, res))