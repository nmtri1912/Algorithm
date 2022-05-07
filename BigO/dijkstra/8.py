import queue
INF = 10 ** 9
MAX = 505

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

while True:
	N, M = map(int, input().split())
	
	if N == 0 and M == 0:
		break
	
	graph = [[] for _ in range(N)]
	graphS = [[] for _ in range(N)]
	graphD = [[] for _ in range(N)]
	dist = [INF] * N
	distS = [INF] * N
	distD = [INF] * N
		
	S, D = map(int, input().split())
	
	for i in range(M):
		u, v, w = map(int, input().split())
		graphS[u].append((w, v))
		graphD[v].append((w, u))
	
	Dijkstra(S, distS, graphS)
	Dijkstra(D, distD, graphD)
	shortestPath = distS[D]
	
	for u in range(N):
		for w, v in graphS[u]:
			if distS[u] + w + distD[v] != shortestPath:
				graph[u].append((w, v))
	
	Dijkstra(S, dist, graph)
	print(dist[D] if dist[D] != INF else -1)