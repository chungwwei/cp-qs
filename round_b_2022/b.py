t = int(input())
for tcs in range(t):
	num = int(input())
	res = 0

	s = set()
	bound = int(num ** 0.5) + 1
	for i in range(1, bound, 1):
		if num % i == 0:
			cand2 = str(num // i)
			cand = str(i)
			s.add(cand)
			s.add(cand2)
	for c in s:
		if c == "".join([n for n in c][::-1]):
			res += 1

	print('Case #{}: {}'.format(tcs + 1, res))
	
		
