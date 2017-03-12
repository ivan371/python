n = int(input())
m = int(input())
adj = [[] for i in range(n)] 
adjT = [[] for i in range(n)]
used = [False for i in range(n)]
uset = set()
color = [int(0) for i in range(n)] 
topSort = [] 
component = [int(0) for i in range(n)] 
graph = [[] for i in range(n)]

for i in range(m):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)    
    v -= 1
    w -= 1
    adj[v].append(w)
    adjT[w].append(v)

def dfs(v) : 
    if used[v]:
        return
    used[v] = True 
    for w in adj[v]:
        dfs(w) 
    topSort.append(v)
     
def dfss (vertex, graph, uset=set()):
    uset.add(vertex)
    for i in graph[vertex]:
        if i not in uset:
            dfss(i, graph, uset)

def ccs(v, componentID):
    if used[v]:
        return
    used[v] = True 
    component[v] = componentID
    for w in adjT[v]:
        ccs(w, componentID) 

def run():
    for v in range(n):
        dfs(v)
    for i in range(n):
        used[i] = False    
    componentID = 0
    for v in reversed(topSort):
        if not used[v]:
            ccs(v, componentID)
            componentID = componentID + 1
    num = 0
    for vert in range(n):
        if vert not in uset:
            dfss(vert, graph, uset)
            num += 1
    print(str(num) + " " + str(componentID)) 
   
run()
