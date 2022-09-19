tcs = int(input())
for tc in range(tcs):
	n = int(input())
	A = []
	C = []
	ids = []
	for _ in range(n):
		arr = input().split()
		color = arr[0]
		durability = int(arr[1])
		id = int(arr[2])
		A.append((color, id))
		C.append((durability, id))
		ids.append(id)

	A.sort()
	C.sort()

	res = 0
	for i in range(n):
		if A[i][1] == C[i][1]:
			res += 1
	
	print('Case #{}: {}'.format(tc + 1, res))