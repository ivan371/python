def dfs (vertex, graph, used=set()):
    used.add(vertex)
    for i in graph[vertex]:
        if i not in used:
            dfs(i, graph, used)

n = int(input())
m = int(input())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = [int(x) for x in input().split()]
    graph[a].append(b)
    graph[b].append(a)
used = set()
num = 0
for vert in range(n):
    if vert not in used:
        dfs(vert, graph, used)
        num += 1

if num == 1:
    print('YES')
else:
    print('NO')
