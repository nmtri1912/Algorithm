import sys
sys.setrecursionlimit(10**6)

def DFS(s, graph, visited):
    visited[s] = True
    for v in graph[s]:
        if not visited[v]:
            DFS(v, graph, visited)

def main():
    MAX = 100000 + 1
    testcase = int(input())
    res = []
    for _ in range(testcase):
        ans = 0
        n = int(input())
        m = int(input())
        graph = [[] for i in range(n)]
        visited = [False for i in range(n)]
        for i in range(m):
            u, v = list(map(int, input().split()))
            graph[u].append(v)
            graph[v].append(u)

        for i in range(n):
            if not visited[i]:
                ans+=1
                DFS(i, graph, visited)
                
        res.append(ans)
    
    for ans in res:
        print(ans)
        
if __name__== "__main__":
    main()