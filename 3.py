#http://codeforces.com/problemset/problem/110/A

freq= [0]*26
s1 = raw_input()
flag = True
for i  in s1:
	freq[ord(i) - 65] += 1
s2 = raw_input()
for i  in s2:
	freq[ord(i) - 65] += 1
data = raw_input()
for i  in data:
	freq[ord(i) - 65] -= 1
for i in freq:
	if i != 0:
		print("NO")
		flag = False
		break
if flag == True:
	print("YES") 
