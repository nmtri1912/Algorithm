from queue import Queue
import collections

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(i , j, matrix, visited, n, m):
    q = Queue()
    q.put(i)
    q.put(j)
    visited[i][j] = True
    size = 0
    if matrix[i][j]:
        size = 1
        
    while not q.empty():
        x = q.get()
        y = q.get()
        for i in range(4):
            u = x + dx[i]
            v = y + dy[i]
            if 0 <= u < n and 0 <= v < m and matrix[u][v] and not visited[u][v]:
                visited[u][v] = True
                size+=1
                q.put(u)
                q.put(v)
    return size

m = 0
n = 0    
        
def main():
    n, m = list(map(int, input().split()))
    
    while m or n:
        res = []
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        visited = [[False for _ in range(m)] for _ in range(n)]
            
        for i in range(n):
            matrix[i] = list(map(int, input().split()))
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] and not visited[i][j]:
                    ans = BFS(i , j, matrix, visited, n, m)
                    res.append(ans)
        fre = dict(collections.Counter(res))
        res = dict(collections.OrderedDict(sorted(fre.items())))
        print(sum(res.values()))
        for k, v in res.items():
            print(f"{k} {v}")
            
        n, m = list(map(int, input().split()))
    
if __name__== "__main__":
    main()