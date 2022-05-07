import queue
INF = 10 ** 9
MAX = 10001
 
def Dijkstra(s, dist, graph):
    pq = queue.PriorityQueue()
    pq.put((0, s))
    dist[s] = 0
     
    while not pq.empty():
        w, u = pq.get()
         
        if w > dist[u]:
            continue
         
        for weight, v in graph[u]:
            if w + weight < dist[v]:
                dist[v] = w + weight
                pq.put((dist[v], v))
 
T = int(input())
 
for _ in range(T):
    n, m, k, s, t = map(int, input().split())
     
    graphS = [[] for _ in range(MAX)]
    graphT = [[] for _ in range(MAX)]
    distT = [INF] * MAX
    distS = [INF] * MAX
     
    for i in range(m):
        u, v, d = map(int, input().split())
        graphS[u].append((d, v))
        graphT[v].append((d, u))
     
    Dijkstra(s, distS, graphS)
    Dijkstra(t, distT, graphT)
    res = distS[t]
     
    for i in range(k):
        u, v, d = map(int, input().split())
        res = min(res, distS[u] + d + distT[v], distS[v] + d + distT[u])
     
    print(res if res != INF else -1)