from queue import Queue

def BFS(s, graph, visited, dist):
    q = Queue()
    q.put(s)
    dist[s] = 0
    visited[s] = True
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                dist[v] = dist[u] + 1
                visited[v] = True
                q.put(v)
            
def main():
    MAX = 1000 + 1
    result = []
    testcase = int(input())
    
    for i in range(testcase):
        
        dist = [-1] * MAX
        visited = [False] * MAX
        graph = [[] for i in range(MAX)]
        
        n, m = list(map(int, input().split()))
        for i in range(m):
            u, v = list(map(int, input().split()))
            graph[u].append(v)
            graph[v].append(u)
        
        s = int(input())
        BFS(s, graph, visited, dist)
        
        ans = []
        for i in range(1, n+1):
            if i != s:
                if visited[i]:
                    ans.append(str(dist[i] * 6))
                else:
                    ans.append(str(-1))
        result.append(ans)
    for ans in result:
        print(' '.join(ans))

if __name__== "__main__":
    main()