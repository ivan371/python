def search_min(tr, vizited):
    min=INF
    for ind in vizited:
        for index, elem in enumerate(tr[ind]):
            if elem>0 and elem<min and index not in vizited:
                min=elem
                index2=index
    return [min, index2]

def prim(matr):
    toVisit=[i for i in range(1,len(matr))]
    vizited=[0]
    result=[0]
    for index in toVisit:
        weight, ind=search_min(matr, vizited)
        result.append(weight)
        vizited.append(ind)
    return result


INF = 10 ** 9
n, m = map(int,input().split())
W = [[0 for j in range (n)] for i in range (n)]
for i in range(m):
    u, v, w = map(int, input().split())
    W[u][v] = w
    W[v][u] = w

print(prim(W))
