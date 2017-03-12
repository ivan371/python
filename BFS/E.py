def bfs_fire(G, start, fired = None):
  if fired is None:
    fired = set()
  fired.add(start)
  time = {start: 0} 
  Q = [start]
  while Q:
     current = Q.pop(0) 
     for neighbour in G[current]:
       if neighbour not in fired:
          fired.add(neighbour)
          Q.append(neighbour)
          print(current, neighbour)
          time[neighbour] = time[current] + 1
       elif neighbour in fired and neighbour != current:
          return(time[neighbour] + 1)
  return -1

n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = [int(x) for x in input().split()]
    graph[a].append(b)
    #graph[b].append(a)
fired=None
cycles = []

for i in range(n):
    cycles.append(bfs_fire(graph,i))

print (cycles)
