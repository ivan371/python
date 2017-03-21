def hamilton(curr):
    Path.append(curr)
    if len(Path) == n:
        if A[Path[0]][Path[-1]] == 1:
            return True
        else:
            Path.pop()
            return False
    Visited[curr] = True
    for next in range(n): 
        if A[curr][next] == 1 and not Visited[next]:
            if hamilton(next):
                return True
    Visited[curr] = False
    Path.pop()

    return False

n, m = map(int,input().split())
A = {}
A = [[0 for j in range (n)] for i in range (n)]
for i in range(m):
    u, v = map(int, input().split())
    A[u][v] = 1
    A[v][u] = 1
Visited = [False] * n
Path = []
if hamilton(0):
    for i in Path:
        print (i, end = ' ')
