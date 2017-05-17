A = []
n, m = map(int, input().split())
for i in range(n):
	a, b = map(int, input().split()) 
	A.append([a, b])
B = {}
for i in range(n):
	B[A[i][0]] = A[i][1]
	B[A[i][1]] = A[i][0]
print(B)
