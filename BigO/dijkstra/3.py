import queue
INF = float('inf')
MAX = 10000 + 5
dist = [INF] * MAX
graph = [[] for _ in range(MAX)]

s = int(input())

for _ in range(s):
    n = int(input())
    idx = 1
    name_dict = {}
    graph = [[] for _ in range(MAX)]
    
    for i in range(1, n + 1):
        name = input()
        name_dict.update({name: idx})
        p = int(input())
        for i in range(p):
            b, w = list(map(int, input().split()))
            graph[idx].append((b, w))
            # graph[b].append((idx, w))
        idx+=1
    
    def dijkstra(start, end):
        pq = queue.PriorityQueue()
        pq.put((0, start))
        dist[start] = 0
        
        while not pq.empty():
            w, b = pq.get()
            if b == end:
                return dist[end]
            for v, new_w in graph[b]:
                if w + new_w < dist[v]:
                    dist[v] = w + new_w
                    pq.put((dist[v], v))
        return dist[end]
        
    r = int(input())
    for _ in range(r):
        name1, name2 = list(map(str, input().split()))
        dist = [INF] * MAX
        start = name_dict[name1]
        end = name_dict[name2]
        print(dijkstra(start, end))
        
    break_line = input()