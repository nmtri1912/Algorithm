from queue import Queue
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def BFS(sx, sy, matrix, visited, n , m):
    ans = 1
    q = Queue()
    q.put(sx)
    q.put(sy)
    visited[sx][sy] = True
    
    while not q.empty():
        x = q.get()
        y = q.get()
        for i in range(4):
            u = x + dx[i]
            v = y + dy[i]
            if 0 <= u < n and 0 <= v < m and matrix[u][v] == '.' and not visited[u][v]:
                visited[u][v] = True
                ans+=1
                q.put(u)
                q.put(v)
    return ans
            
def main():
    res = []
    test_case = int(input())
    for _ in range(test_case):
        m, n = list(map(int, input().split()))
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            matrix[i] = [e for e in input()]
        sx = -1
        sy = -1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '@':
                    sx = i
                    sy = j
        ans = BFS(sx, sy, matrix, visited, n, m)
        res.append(ans)
        
    for i in range(1, len(res) + 1):
        print(f"Case {i}:",res[i-1])
    

if __name__== "__main__":
    main()