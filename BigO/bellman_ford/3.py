import queue
INF = 10 ** 9
energy = [0] * 105

def hasPathBFS(s, f):
    visited = [False] * (n + 1)
    q = queue.Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()
        for edge in graph:
            edge_u, edge_v = edge
            if edge_u == u:
                v = edge_v
                if not visited[v]:
                    visited[v] = True
                    q.put(v)
                if v == f:
                    return True
    return False

def bellman_ford(s, f):
    dist = [-INF] * (n + 1)
    dist[s] = 100

    for i in range(n - 1):
        for edge in graph:
            u, v = edge
            if dist[u] > 0:
                dist[v] = max(dist[v], dist[u] + energy[v])
    
    for edge in graph:
        u, v = edge
        if dist[u] > 0 and dist[u] + energy[v] > dist[v] and hasPathBFS(u, f):
            return True
    
    return dist[f] > 0
            
while True:
    n = int(input())
    if n == -1:
        break
    
    graph = []

    for u in range(1, n + 1):
        line = list(map(int, input().split()))
        energy[u] = line.pop(0)

        if not line:
            line.extend(list(map(int, input().split())))

        m = line.pop(0)

        while len(line) != m:
            line.extend(list(map(int, input().split())))
        
        for v in line:
            graph.append((u, v))
        
    is_possible = bellman_ford(1, n)
    print("winnable" if is_possible else "hopeless")