import sys
sys.setrecursionlimit(10**6)

def DFS(n, m, i, j, matrix, visited, temp, is_ocean):
    pass

def main():
    test_case = int(input())
    for _ in range(test_case):
        n, m = list(map(int , input().split()))
        graph = [[] for i in range(n)]
        visited = [False * n]
        path = [-1 * n]
        
        for i in range(m):
            u, v = list(map(int , input().split()))
            if v not in graph[u]:
                graph[u].append(v)
        
        DFS(1)
    
if __name__== "__main__":
    main()