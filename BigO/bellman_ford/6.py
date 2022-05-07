INF = 10 ** 9


def bellman_ford(s):
    dist = [INF] * (n + 1)
    dist[s] = 0

    for i in range(n):
        for edge in graph:
            u, v, w = edge
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for j in range(len(graph)):
        u, v, w = graph[j]
        if dist[u] != INF and dist[u] + w < dist[v]:
            return True
    
    return False


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    graph = []

    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, -w))
    
    print("Yes" if bellman_ford(1) else "No")