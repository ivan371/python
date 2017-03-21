n, m = map(int, input().split()) 
adj = [[] for i in range(n)] 
color = [int(0) for i in range(n)] 
topSort = [] 

for i in range(m):
    v, w = map(int, input().split())
    adj[v].append(w)

def topologicalSort(v) :
    if color[v] == 2:
        return True
    if color[v] == 1:
        return False
    color[v] = 1 
    for w in adj[v]:
        if not topologicalSort(w):
            return False
    color[v] = 2 
    topSort.append(v)
    return True
     
def run():
    cyclic = False 
    for v in range(n):
        if not topologicalSort(v):
            cyclic = True
    if not cyclic:
        topSort.reverse()
        for v in topSort:
            print(v, end=' ')
    else:
        print('NO')

run()
