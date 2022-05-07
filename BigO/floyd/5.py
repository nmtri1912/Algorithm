max_cost = [[None] * 81 for _ in range(81)]
INF = 10 ** 9
t = 1

def floy():
    for _ in range(2):
        for k in range(1, c + 1):
            for i in range(1, c + 1):
                for j in range(1, c + 1):
                    max_point = max(max_cost[i][k], max_cost[k][j])
                    if dist[i][j] + max_cost[i][j] > dist[i][k] + dist[k][j] + max_point:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        max_cost[i][j] = max_point

while True:
    c, r, q = map(int, input().split())
    if not c:
        break
    
    f = [0] + list(map(int, input().split()))
    
    for i in range(1, c + 1):
        for j in range(1, c + 1):
            max_cost[i][j] = max(f[i], f[j])

    dist = [[INF] * (c + 1) for _ in range(c + 1)]

    for _ in range(r):
        u, v, w = map(int, input().split())
        dist[u][v] = dist[v][u] = w
    
    floy()

    if t > 1:
        print()
    
    print('Case #{}'.format(t))
    t += 1

    for _ in range(q):
        u, v = map(int, input().split())
        print(-1 if dist[u][v] == INF else dist[u][v] + max_cost[u][v])