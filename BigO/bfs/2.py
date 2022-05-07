from queue import Queue
dx = [-1,1,0,0]
dy = [0,0,-1,1]
sx = -1
sy = -1
ex = -1
ey = -1

def check(m, n, matrix, value):
    cnt = 0
    for i in range(m):
        for j in range(n):
            if (i == 0 or i == m-1 or j == 0 or j == n-1) and matrix[i][j]=='.':
                cnt+=1
                if cnt == 1:
                    value.update({'sx': i, 'sy': j})
                if cnt == 2:
	                value.update({'ex': i, 'ey': j})
                if cnt > 2:
                    return False
    if cnt == 2:
        return True
    return False

def BFS(m, n, sx, sy, ex, ey, matrix, visited):
    q = Queue()
    q.put(sx)
    q.put(sy)
    visited[sx][sy] = True
    
    while not q.empty():
        x = q.get()
        y = q.get()
        if x == ex and y == ey:
            return True
        for i in range(len(dx)):
                u = x + dx[i]
                v = y + dy[i]
                if 0 <= u < m and 0 <= v < n and matrix[u][v] == '.' and not visited[u][v]:
                    visited[u][v] = True
                    q.put(u)
                    q.put(v)
    return False
    
def main():
    testcase = int(input())
    ans = []
    for _ in range(testcase):
        m, n = list(map(int, input().split()))
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            matrix[i] = [e for e in input()]
            
        value = dict({'sx': - 1, 'sy': -1, 'ex': -1, 'ey': -1})
        if not check(m,n,matrix, value):
            ans.append("invalid")
            continue
        
        res = BFS(m, n, value['sx'], value['sy'], value['ex'], value['ey'], matrix, visited)
        if res:
            ans.append("valid")
        else:
            ans.append("invalid")
            
    for e in ans:
        print(e)
    

if __name__== "__main__":
    main()