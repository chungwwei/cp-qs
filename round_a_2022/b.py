
t = int(input())
for tcs in range(t):
	num = input()
	original = int(num)
	
	last = int(num[-1])
	res = float('inf')
	n = len(num)

	total = 0
	for c in num:
		total += int(c)

	if len(num) == 1:
		for i in range(0, 10, 1):
			if (total + i) % 9 == 0:
				cand = str(i) + num
				cand = int(cand)
				cand2= num + str(i)
				cand2= int(cand2)
				if cand > original:
					res = min(res, cand)
				if cand2 > original:
					res = min(res, cand2)
	else:
		for i in range(0, 10, 1):
			if (total + i) % 9 == 0:
				if i >= last: 
					cand = num + str(i)
					cand = int(cand)
					res = min(res, cand)
				else:
					cand = num[:n - 1] + str(i) + str(last)
					cand = int(cand)
					res = min(res, cand)
	print('Case #{}: {}'.format(tcs + 1, res))
		
