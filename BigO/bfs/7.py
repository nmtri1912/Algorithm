from queue import Queue
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(n, m, sx, sy, ex, ey, matrix):
    q = Queue()
    q.put(sx)
    q.put(sy)
    
    while not q.empty():
        x = q.get()
        y = q.get()
        for i in range(4):
            u = x + dx[i]
            v = y + dy[i]
            if u == ex and v == ey and matrix[u][v] == 'X':
                return True
            if 0 <= u < n and 0 <= v < m and matrix[u][v] == '.':
                matrix[u][v] = 'X'
                q.put(u)
                q.put(v)
    
    return False
    
def main():
    n, m = list(map(int, input().split()))
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        matrix[i] = [e for e in input()]
    sx, sy = list(map(int, input().split()))
    ex, ey = list(map(int, input().split()))
    check = BFS(n , m, sx - 1, sy - 1, ex - 1, ey - 1, matrix)
    if check:
        print("YES")
    else:
        print("NO")

if __name__== "__main__":
    main()