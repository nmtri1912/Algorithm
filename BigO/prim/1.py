import queue

def prim(s):
    dist = [10 ** 9] * (N + 1)
    visited = [False] * (N + 1)
    pq = queue.PriorityQueue()
    pq.put((0, s))
    dist[s] = 0

    while not pq.empty():
        w, u = pq.get()
        visited[u] = True

        for new_w, new_v in graph[u]:
            if not visited[new_v] and new_w < dist[new_v]:
                dist[new_v] = new_w
                pq.put((new_w, new_v))
    
    res = 0
    for i in range(1, N + 1):
        if not visited[i]:
            continue
        res += dist[i]
    return res

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

print(prim(N))