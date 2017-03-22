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


Main = []
Main = input().split()
for i in range(len(Main)):
    Main[i] = int(Main[i])
n = Main.pop(0)
m = Main.pop(0)
d = {}
for i in range(n):
    d[i] = {}

for i in range(m):
    u, v, w = map(int, input().split())
    d[u][v] = w
    d[v][u] = w

dic = {}
for i in range(n):
    dic[i] = dijkstra(d, i)

for i in range(n):
    d_c = float('+inf')
    ver = 0
    for v in Main:
        if float(dic[i][v]) < d_c:
            ver = v
    print(v)
 
