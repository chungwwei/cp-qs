tcs = int(input())
for tc in range(tcs):
	A = input().split()
	L, N = int(A[0]), int(A[1])
	arr = []
	for _ in range(N):
		temp = input().split()
		unit = int(temp[0])
		dir = temp[1]
		arr.append((unit, dir))

	res = 0
	total = 0
	cur_dir = arr[0][1]
	for unit, dir in arr:
		if dir == cur_dir:
			total += unit * 1 if dir == "C" else -1
			cnt = total // L
			total = total % L
			res += cnt
			cur_dir = dir
		else:
			total += unit * 1 if dir == "C" else -1
			cur_dir = dir

	print('Case #{}: {}'.format(tc + 1, res))


