n = int(input())
A = []
for i in range(n):
	A.append(list(int(x) for x in input().split()))
B = []
sum = 0
for i in range(n):
	for j in range(n):
		if A[i][j] == 1 :
			sum += 1
	B.append(sum)
	sum = 0
print(B)
