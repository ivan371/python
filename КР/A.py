n = int(input())

A = [[0 for i in range(n)] for j in range(n)]
B = [0 for i in range(n)]
for i in range(n):
    A[i] = input().split()

B = input().split()

sum = 0
for i in range(n):
    for j in range(n):
        if A[i][j] == '1':
            if B[i] != B[j]:
                sum += 1
print(int(sum / 2))
