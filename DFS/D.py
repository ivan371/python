
n = int(input())
m = int(input())
adj = [[] for i in range(n)] 
used = [False for i in range(n)] 
   
for i in range(m):
    v, w = map(int, input().split())
    v -= 1
    w -= 1
    adj[v].append(w)
    adj[w].append(v)

print(   

def dfs(v): 
    if used[v]: 
        return
    used[v] = True 
    for w in adj[v]:
        dfs(w) 
       
dfs(v)
res = 'YES'
for i in range(n):
    if not used[i]:
        res = 'NO'
        break

print(res)
