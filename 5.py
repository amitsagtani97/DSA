#http://codeforces.com/problemset/problem/71/A
for i in range(input()):
	x = raw_input()
	if(len(x) > 10):
		c = x[0] + str(len(x) - 2) + x[-1]
		print(c)
	else:
		print(x)