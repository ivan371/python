sub = input()
big = input()
l = len(sub)
A = []
for i in range (len(big)):
	#print(big[i:l])
	#print(big[i:l+i])
	if sub in big[i:l+i] and l+i <= len(big):
		A.append(i)
if len(A) == 0:
	print (-1)
else:
	print(" ".join(map(str, A)))
