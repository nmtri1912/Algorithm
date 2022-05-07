import queue
 
def Dijkstra(s):
    dist = [10 ** 9] * N
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
     
    return dist
 
T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    R = int(input())
    graph = [[] for _ in range(N)]
     
    for _ in range(R):
        u, v = map(int, input().split())
        graph[u].append((1, v))
        graph[v].append((1, u))
     
    s, d = map(int, input().split())
    distS = Dijkstra(s)
    distD = Dijkstra(d)
    res = 0
     
    for i in range(N):
        res = max(res, distS[i] + distD[i])
     
    print("Case {}: {}".format(t, res))