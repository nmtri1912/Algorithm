import sys
sys.setrecursionlimit(10**6)

def DFS(s, visited, graph, dist):
    visited[s] = True
    for v in graph[s]:
        if not visited[v]:
            dist[v] = dist[s] + 1
            DFS(v, visited, graph, dist)

def main():
    MAX = 1000 + 1
    dist = [-1] * MAX
    visited = [False] * MAX
    graph = [[] for i in range(MAX)]
    n = int(input())
    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)
        
    DFS(1, visited, graph, dist)
    
    min_id = n
    min_dist = n
    q = int(input())
    
    for _ in range(q):
        qi = int(input())
        if dist[qi] < min_dist or (dist[qi] == min_dist and qi < min_id):
            min_dist = dist[qi]
            min_id = qi
    print(min_id)
    
if __name__== "__main__":
    main()