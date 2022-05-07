def floy():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])

t = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    dist = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    arr = []

    for _ in range(N):
        arr.append(input().strip())
    
    M = int(input())
    for _ in range(M):
        source, rate, dest = input().split()
        u, v = map(lambda x: arr.index(x), (source, dest))
        dist[u][v] = float(rate)
    input()

    floy()

    arbitrage = False
    for i in range(N):
        if dist[i][i] > 1:
            arbitrage = True
            break
    
    print('Case {}: {}'.format(t, "Yes" if arbitrage else "No"))
    t += 1