def tsp_permutations(G):

   min_path_length=1e300   # устанавливаем минимальную длину в бесконечность
   min_path=[]
   start_node=G.nodes()[0] # Фиксируем начальный узел (сокращаем перебор).
   for path in xpermutations(G.nodes()[1:]): # перебор всех узлов кроме первого.
       path.insert(0,start_node)    # добавляем в начало пути стартовый узел
       path_length=0                # обнуляем длину текущего пути  
       path_is_ok=1                 # Сначала считаем, что путь проходим
       for i in range(0,len(path)):
           v1=path[i]   #выбираем ребро (v1,v2), для текущей вершины
           if i<len(path)-1:      
               v2=path[i+1]
           else:
               v2=path[0]           # Если нода-последняя, то замыкаем путь. 

           if G.has_edge(v1,v2):
               path_length=path_length+G.get_edge(v1,v2)        
           else:  
               path_is_ok=0  # нет ребра (v1,v2) - путь непроходим.
               break 
       if (path_is_ok):
               print (path, path_length)
               if min_path_length>path_length:
                   min_path_length=path_length        
                   min_path=path        
   print ("Optimal path:",min_path, min_path_length)
   return min_path      

n, m = map(int,input().split())
A = [[0 for j in range (n)] for i in range (n)]
for i in range(m):
    u, v, w = map(int, input().split())
    A[u][v] = w
Visited = [False] * n
Path = []

