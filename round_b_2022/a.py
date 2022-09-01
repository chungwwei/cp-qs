import math

t = int(input())
for tcs in range(t):
	I = [int(n) for n in input().split()]
	R, A, B = I[0], I[1], I[2]

	areas = 0
	right = True
	while R > 0:
		a = math.pi * R ** 2
		if right:
			areas += a
			right = False
			R = R * A
		else:
			areas += a
			right = True
			R = R // B

	print('Case #{}: {}'.format(tcs + 1, areas))
	
		
