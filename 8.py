n = int(input())
A = []
for i in range(n):
        A.append([int(x) for x in input().split()])
print(A)
B = [[] for i in range(n)]
for i in range(n):
	C = A[i]
	for j in C:
		B[j].append(i)
print(B)
