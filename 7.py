n = int(input())
A = []
for i in range(n):
	A.append(int(x) for x in input().split())
B = [[0] * n for i in range(n)]
for i in range(n):
	C = list(A[i])
	for j in C:
		B[i][j] = 1
		for k in A[j]:
			B[i][k] = 1
print(B)
