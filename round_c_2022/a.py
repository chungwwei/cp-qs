
tcs = int(input())
for tc in range(tcs):
	N = int(input())
	s = input()

	has_num = False
	has_lower = False
	has_upper = False
	has_special = False

	res = []
	for c in s:
		if c.isdigit():
			has_num = True
		if c.islower():
			has_lower = True
		if c.isupper():
			has_upper = True
		if c in "#@*&":
			has_special = True
		res.append(c)
	
	if not has_num:
		res.append('0')
	if not has_lower:
		res.append('a')
	if not has_upper:
		res.append('A')
	if not has_special:
		res.append('#')

	while len(res) < 7:
		res.append('*')
	
	print('Case #{}: {}'.format(tc + 1, ''.join(res)))