n = int(input())
m = int(input())

A = []

for i in range(m):
    k, l = map(int, input().split())
    A.append([k, l])

B = [0 for i in range (n)]
for i in range(m):
    B[A[i][0]]+=1
    B[A[i][1]]+=1
res = 'YES'
for i in range(n):
    if B[i] % 2 == 1:
        res = 'NO'
        break
print (res)
