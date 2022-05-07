import queue
INF = float('inf')
MAX = 10 ** 5 + 1

graph = [[] for _ in range(MAX)]
dist1 = [INF] * MAX
dist2 = [INF] * MAX

N, M, k, x = list(map(int, input().split()))

available = list(map(int, input().split()))

for i in range(M):
    u, v, w = list(map(int, input().split()))
    graph[u].append((v, w))
    graph[v].append((u, w))
    
S, T = list(map(int, input().split()))


def dijkstra(start, dist):
    pq = queue.PriorityQueue()
    dist[start] = 0
    pq.put((0, start))
    
    while not pq.empty():
        w, b = pq.get()
        if w != dist[b]:
            continue
        for v, new_w in graph[b]:
            if w + new_w < dist[v]:
                dist[v] = w + new_w
                pq.put((dist[v], v))

dijkstra(S, dist1)
dijkstra(T, dist2)

ans = INF

for i in range(len(available)):
    if dist2[available[i]] < x:
        ans = min(ans, dist2[available[i]] + dist1[available[i]])

if ans == INF:
    print(-1)
else:
    print(ans)