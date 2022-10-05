from collections import Counter

t = int(input())
for tcs in range(t):
	I = input()
	P = input()

	if len(P) < len(I):
		print('Case #{}: {}'.format(tcs + 1, "IMPOSSIBLE"))
		continue

	i_stk = []
	p_stk = []

	n = len(I)
	chars = set()
	for i in range(n - 1, -1, -1):
		i_stk.append(I[i])
		chars.add(I[i])
	n = len(P)
	for i in range(n - 1, -1, -1):
		p_stk.append(P[i])
	
	res = 0
	while i_stk and p_stk:
		if i_stk[-1] not in chars:
			flag = False
			break
		if i_stk[-1] == p_stk[-1]:
			i_stk.pop()
			p_stk.pop()
		elif i_stk[-1] != p_stk[-1]:
			p_stk.pop()
			res += 1

	res += len(p_stk)
	if len(i_stk) == 0:
		print('Case #{}: {}'.format(tcs + 1, res))
	else:
		print('Case #{}: {}'.format(tcs + 1, "IMPOSSIBLE"))
	
		
