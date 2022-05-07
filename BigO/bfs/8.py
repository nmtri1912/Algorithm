from queue import Queue
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count_sheepy = 0
count_wolf = 0

def BFS(n, m, i, j, visited, matrix):
    sheepy = 0
    wolf = 0
    q = Queue()
    q.put(i)
    q.put(j)
    visited[i][j] = True
    out_side = False
    while not q.empty():
        x = q.get()
        y = q.get()
        if matrix[x][y] == 'k':
            sheepy+=1
        if matrix[x][y] == 'v':
            wolf+=1
        if  x == 0 or x == n-1 or y == 0 or y == m-1:
            out_side = True
        for i in range(4):
            u = x + dx[i]
            v = y + dy[i]
            if 0 <= u < n and 0 <= v < m and matrix[u][v] != '#' and not visited[u][v]:
                visited[u][v] = True
                q.put(u)
                q.put(v)
    if out_side:
        return sheepy, wolf
    else:
        if sheepy > wolf:
            return sheepy, 0
        else:
            return 0, wolf

def main():
    n, m = list(map(int, input().split()))
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        matrix[i] = [e for e in input()]
        
    count_sheepy = 0
    count_wolf = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != '#' and not visited[i][j]:
                nsheepy, nwolf = BFS(n, m, i, j, visited, matrix)
                count_sheepy+=nsheepy
                count_wolf+=nwolf
                
    print(count_sheepy, count_wolf)
    
if __name__== "__main__":
    main()
