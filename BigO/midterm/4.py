import queue
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def BFS(R, C, sx, sy, ex, ey, matrix, dist):
    q = queue.Queue()
    q.put(sx)
    q.put(sy)
    dist[sx][sy] = 1
    
    while not q.empty():
        u = q.get()
        v = q.get()
        if u == ex and v == ey:
            return dist[u][v] - 1
        for i in range(4):
            x = u + dx[i]
            y = v + dy[i]
            if x in range(R) and y in range(C) and dist[x][y] == 0:
                dist[x][y] = dist[u][v] + 1
                q.put(x)
                q.put(y)
    return -1

R, C = list(map(int, input().split()))

while R and C:
    matrix = [[0 for _ in range(C)] for _ in range(R)]
    dist = [[0 for _ in range(C)] for _ in range(R)]

    n = int(input())
    for i in range(n):
        arr = list(map(int, input().split()))
        index_row = arr[0]
        qty = arr[1]
        for j in range(2, qty + 2):
            index_column = arr[j]
            dist[index_row][index_column] = -1
    sx, sy = list(map(int, input().split()))
    ex, ey = list(map(int, input().split()))
    print(BFS(R, C, sx, sy, ex, ey, matrix, dist))
    
    R, C = list(map(int, input().split()))
    