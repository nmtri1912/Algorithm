INF = 10 ** 9

def bellman_ford(s):
    dist[s] = 0
    for i in range(n - 1):
        for edge in graph:
            u, v, w = edge
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for i in range(n):
        for edge in graph:
            u, v, w = edge
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = -INF

T = int(input())

for t in range(1, T + 1):
    input()
    n = int(input())
    weight = [0] + list(map(int, input().split()))
    m = int(input())
    
    graph = []
    dist = [INF] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        graph.append((u, v, (weight[v] - weight[u]) ** 3))
    
    bellman_ford(1)
    q = int(input())
    print("Case {}:".format(t))

    for _ in range(q):
        f = int(input())
        print(dist[f] if dist[f] != INF and dist[f] >= 3 else "?")