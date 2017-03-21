INF = 10 ** 9
n, m = map(int,input().split())
W = [[INF for j in range (n)] for i in range (n)]
for i in range(m):
    u, v, w = map(int, input().split())
    W[u][v] = w
    W[v][u] = w

dist = [INF] * n
pars = [0] * n
dist[0] = 0
used = [False] * n
ans = 0
for i in range(n):
    min_dist = INF
    for j in range(n):
        if not used[j] and dist[j] < min_dist:
            min_dist = dist[j]
            u = j
    ans += min_dist
    used[u] = True
    for v in range(n):
        if dist[v] > W[u][v]:
            dist[v] = W[u][v]
            pars[v] = [u, v]
        #dist[v] = min(dist[v], W[u][v])

print (ans)
pars[1][0] = 0
for i in range(1, n):
    print(pars[i][0], pars[i][1])
#print (pars)
