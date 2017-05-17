A = []
n, m = map(int, input().split())
for i in range(m):
	a, b, c = map(int, input().split())
	A.append([a, b, c])
B = {}
for i in range(n):
	B[A[i][0]] = {A[i][1]: A[i][2]}
print(B)
