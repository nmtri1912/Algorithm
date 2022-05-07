import queue
INF = float('inf')
MAX = 50000 + 5

Q = int(input())

for count in range(1, Q+1):
    N, M, S, T = list(map(int, input().split()))
    graph = [[] for _ in range(MAX)]
    dist = [INF] * MAX
    for i in range(M):
        a, b, w = list(map(int, input().split()))
        graph[a].append((b,w))
        graph[b].append((a,w))
    
    def dijkstra(start, end):
        pq = queue.PriorityQueue()
        dist[start] = 0
        pq.put((0, start))
        
        while not pq.empty():
            w, b = pq.get()
            if b == end:
                return dist[end]
            for v, new_w in graph[b]:
                if w + new_w < dist[v]:
                    dist[v] = w + new_w
                    pq.put((dist[v], v))
        return dist[end]
    
    ans = dijkstra(S, T)
    if ans == INF:
        ans = 'unreachable'
    
    print(f"Case #{count}: {ans}")
    