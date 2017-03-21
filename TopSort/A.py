def topologicalSort(v) :
    if color[v] == 2:
        return False
    if color[v] == 1:
        return True
    color[v] = 1 
    for w in adj[v]:
        if not topologicalSort(w):
            return True
    color[v] = 2 
    topSort.append(v)
    return False

def cycl():
    cyclic = False 
    for v in range(n):
        if topologicalSort(v):
            cyclic = True
    if cyclic:
        topSort.reverse()
        for v in topSort:
            print(v, end=' ')
    else:
        print('YES')        
n, m = map(int, input().split()) 
adj = [[] for i in range(n)] 
color = [int(0) for i in range(n)] 
topSort = [] 

for i in range(m):
    v, w = map(int, input().split())
    adj[v].append(w)

cycl()
