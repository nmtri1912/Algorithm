n = 20
t = 1
INF = 10 ** 9

def floy():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

while True:
    try:
        dist = [[INF] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n):
            for j in list(map(int, input().split()))[1:]:
                dist[i][j] = dist[j][i] = 1
        
        floy()
        
        print("Test Set #{}".format(t))
        t += 1

        q = int(input())
        for _ in range(q):
            u, v = map(int, input().split())
            print('{:2d} to {:2d}: {}'.format(u, v, dist[u][v]))
        print()

    except EOFError:
        break