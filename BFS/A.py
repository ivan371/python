from heapq import*
def dijkstra(G, start):
    d = {v: float('+inf') for v in G}
    d[start] = 0
    Q = [(0, start)]
    used = set()
    while len(used) != len(G):
        d_c, current = heappop(Q)
        if d_c != d[current]:
            continue
        for neighbour in G[current]:
            l = d[current] + G[current][neighbour]
            if l < d[neighbour]:
                d[neighbour] = l
                heappush(Q, (l, neighbour))
        used.add(current)
    return d

n, m = map(int,input().split())
d = {}

for i in range(n):
    d[i] = {}
for i in range(m):
    u, v = map(int, input().split())
    d[u][v] = 1
    d[v][u] = 1

dic = dijkstra(d, 0)
for i in range(n):
    print(dic[i])
