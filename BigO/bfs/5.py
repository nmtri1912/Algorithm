from queue import Queue
MAX = 10**5 + 1

def BFS(s, graph, visited, dist, m, has_cat):
    ans = 0
    q = Queue()
    q.put(s)
    visited[s] = True
    if has_cat[s-1]:
        dist[s] = 1
    
    while not q.empty():
        u = q.get()
        if len(graph[u]) == 1 and visited[graph[u][0]] == 1 and dist[u] <= m:
            ans+=1
        for v in graph[u]:
            if not visited[v]:
                if has_cat[v-1]:
                    dist[v] = dist[u] + 1
                elif dist[u] > m:
                    dist[v] = dist[u]
                visited[v] = True
                q.put(v)
    print(ans)
    
def main():
    visited = [False] * MAX
    dist = [0] * MAX
    graph = [[] for i in range(MAX)]
    n, m = list(map(int, input().split()))
    has_cat = list(map(int, input().split()))
    for i in range(n - 1):
        u, v = list(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)
    BFS(1, graph, visited, dist, m, has_cat)

if __name__== "__main__":
    main()