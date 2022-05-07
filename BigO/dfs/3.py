import sys
sys.setrecursionlimit(10**6)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(n, m, i, j, matrix, visited, temp):
    global is_ocean
    visited[i][j] = True
    temp.append((i , j))
    if i == 0 or j == 0 or i == n - 1 or j == m - 1:
        is_ocean = True
    for k in range(4):
        u = i + dx[k]
        v = j + dy[k]
        if u in range(n) and v in range(m) and matrix[u][v] == '.' and not visited[u][v]:
            DFS(n, m ,u ,v ,matrix, visited, temp)
    if not is_ocean:
        return temp
    return None

def main():
    n, m , k = list(map(int, input().split()))
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        matrix[i] = [e for e in input()]
    lakes = []
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and matrix[i][j] == '.':
                
                global is_ocean
                is_ocean = False
                temp = []
                res = DFS(n, m, i, j, matrix, visited, temp)
                if res:
                    lakes.append(res)
                    
    lakes.sort(key=lambda lake: len(lake))
    sum_cell = 0
    for i in range(len(lakes) - k):
        sum_cell += len(lakes[i])
        for r, c in lakes[i]:
            matrix[r][c] = '*'

    print(sum_cell)
    for i in range(n):
        print(''.join(matrix[i]))
if __name__== "__main__":
    main()