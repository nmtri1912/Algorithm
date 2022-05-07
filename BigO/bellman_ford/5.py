INF = 10 ** 9

def bellman_ford(s):
    dist[s] = 0

    for i in range(n - 1):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for i in range(n - 1):
        for j in range(m):
            u, v, w = graph[j]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF


while True:
    n, m, q, s = map(int, input().split())
    
    if n == 0:
        break
    graph = []
    
    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, w))
    
    dist = [INF] * n
    bellman_ford(s)

    for _ in range(q):
        idx = int(input())
    
        if dist[idx] == INF:
            print("Impossible")
        elif dist[idx] == -INF:
            print("-Infinity")
        else:
            print(dist[idx])
    print()