from heapq import*
def dijkstra(G, start, end):
    d = {v: float('+inf') for v in G}
    d[start] = 0
    Q = [(0, start)]
    used = set()
    vs = {v: [] for v in G}
    while len(used) != len(G):
        d_c, current = heappop(Q)
        if d_c != d[current]:
            continue
        if current == end:
            break
        for neighbour in G[current]:
            l = d[current] + G[current][neighbour]
            t = []
            t = vs[current].copy()
            t.append(neighbour)
            if l < d[neighbour]:
                d[neighbour] = l
                vs[neighbour] = t
                heappush(Q, (l, neighbour))
        used.add(current)
    return vs


A = [[0 for i in range(8)] for j in range(8)]
cur = 96
for i in range(1, 9):
    for j in range(1, 9):
        A[i - 1][j - 1] = chr(cur + i) + str(j)

B = {}

for i in range(1, 9):
    for j in range(1, 9):
        B[A[i - 1][j - 1]] = {}

for i in range(1, 9):
    for j in range(1, 9):
        if j - 2 > 0 and i - 1 > 0:
            B[chr(cur + i) + str(j)][chr(cur + i - 1) + str(j - 2)] = 1
        if j - 1 > 0 and i - 2 > 0:
            B[chr(cur + i) + str(j)][chr(cur + i - 2) + str(j - 1)] = 1
        if j + 1 < 9 and i - 2 > 0:
            B[chr(cur + i) + str(j)][chr(cur + i - 2) + str(j + 1)] = 1
        if j - 2 > 0 and i + 1 < 9:
            B[chr(cur + i) + str(j)][chr(cur + i + 1) + str(j - 2)] = 1
        if j - 1 > 0 and i + 2 < 9:
            B[chr(cur + i) + str(j)][chr(cur + i + 2) + str(j - 1)] = 1
        if j + 2 < 9 and i - 1 > 0:
            B[chr(cur + i) + str(j)][chr(cur + i - 1) + str(j + 2)] = 1
        if j + 2 < 9 and i + 1 < 9:
            B[chr(cur + i) + str(j)][chr(cur + i + 1) + str(j + 2)] = 1
        if j + 1 < 9 and i + 2 < 9:
            B[chr(cur + i) + str(j)][chr(cur + i + 2) + str(j + 1)] = 1

x = str(input())
y = str(input())

dic = dijkstra(B, x, y)
print(x)
for i in dic[y]:
    print(i)       

      
