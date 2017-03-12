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
                Q.appent(neighbour)
                print(current, neighbour)
                time[neighbour] = time[current] + 1
