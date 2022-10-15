
tcs = int(input())
for tc in range(tcs):
	Rs, Rh = [int(n) for n in input().split()]
	N = int(input())
	A = []
	for _ in range(N):
		temp = [int(n) for n in input().split()]
		temp = tuple(temp)
		A.append(temp)
	
	M = int(input())
	B = []
	for _ in range(M):
		temp = [int(n) for n in input().split()]
		temp = tuple(temp)
		B.append(temp)

	mx = Rs + Rh
	def collision(p):
		x1, y1 = p
		distance = (x1 ** 2 + y1 ** 2) ** 0.5
		return distance <= mx

	def distance(p):
		x1, y1 = p
		return (x1 ** 2 + y1 ** 2) ** 0.5

	in_house = []
	for i, pair in enumerate(A):
		if collision(pair):
			d = distance(pair)
			in_house.append((d, pair, "R"))
	for i, pair in enumerate(B):
		if collision(pair):
			d = distance(pair)
			in_house.append((d ,pair, "Y"))
	
	in_house.sort()
	# print(in_house)

	red, yellow = 0, 0
	n = len(in_house)
	if n > 0:
		d, pair, C = in_house[0]
		pts = 0
		for i in range(n):
			d, pair, c = in_house[i]
			if c != C:
				break
			pts += c == C
		
		if C == 'R':
			red = pts
		if C == 'Y':
			yellow = pts
		print('Case #{}: {} {}'.format(tc + 1, red, yellow))
	else:
		print('Case #{}: {} {}'.format(tc + 1, 0, 0))




	# first_red = -1
	# first_yellow = -1
	# for i in range(len(in_house)):
	# 	d, pair, c = in_house[i]
	# 	if first_red != -1 and c == 'R':
	# 		first_red = i
	# 	if first_yellow != -1 and c == 'Y':
	# 		first_yellow = i
	
