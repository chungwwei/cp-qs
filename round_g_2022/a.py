from collections import defaultdict

tcs = int(input())
for tc in range(tcs):
	M, N, P = [int(n) for n in input().split()]
	arr = []
	john = []
	for i in range(1, M + 1):
		temp = [int(n) for n in input().split()]
		if P == i:
			john = temp[:]
		arr.append(temp)
	
	cols = defaultdict(int)
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			cols[j] = max(cols[j], arr[i][j])
	
	# print(cols)
	# print(john)
	res = 0
	for i in range(len(john)):
		if john[i] < cols[i]:
			res += abs(john[i] - cols[i])

	print('Case #{}: {}'.format(tc + 1, res))