import queue

INF = float('inf')

N = int(input())
E = int(input())
T = int(input())
M = int(input())


MAX = 100 + 5
graph = [[] for _ in range(MAX)]
dist = [INF] * MAX

def dijkstra(start, end):
    pq = queue.PriorityQueue()
    dist[start] = 0
    pq.put((start, 0))
    
    while not pq.empty():
        b, w = pq.get()
        if b == end:
            return dist[end]
        for new_v, new_w in graph[b]:
            if w + new_w < dist[new_v]:
                dist[new_v] = w + new_w
                pq.put((new_v, dist[new_v]))
    return dist[end]

for _ in range(M):
    a, b, w = list(map(int, input().split()))
    graph[a].append((b, w))

ans = 0
for i in range(N):
    dist = [INF] * MAX
    dist = dijkstra(i+1, E)
    if dist <= T:
        ans += 1
    
print(ans)
