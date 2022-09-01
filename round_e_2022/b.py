tcs = int(input())
for tc in range(tcs):
	n = int(input())
	A = [int(n) for n in input().split()]
	# cap = [n * 2 for n in A]
	arr = [(n, i) for i, n in enumerate(A)]
	arr.sort()
	res = []
	for i in range(n):
		C = A[i] * 2

		# indices
		lo, hi = 0, n - 1
		while lo < hi:
			mid = lo + (hi - lo + 1) // 2
			if arr[mid][0] <= C:
				lo = mid
			else:
				hi = mid - 1
		
		j = lo
		while j >= 0:
			if arr[j][1] != i:
				res.append(str(arr[j][0]))
				break
			j -= 1
	
		if j == -1:
			res.append(str(-1))

		# for j in range(lo, -1, -1):
		# 	if arr[j][1] != i:
		# 		res.append(str(arr[j][0]))
		# 		break
				

				
	
	print('Case #{}: {}'.format(tc + 1, " ".join(res)))