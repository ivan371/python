n = int(input())
A = []
res = [[0] * n for i in range(n)]
for i in range(n):
        A.append(tuple(int(x) for x in input().split()))
for i in range(n):
        for j in A[i]:
                res[i][j] = 1
                res[j][i] = 1 #if graph not oriented the program must be without this string

print(res)



