import queue

class Node:
    def __init__(self, b, w):
        self.b = b
        self.w = w
        
    def __lt__(self, other):
        return self.w < other.w

ptive_inf = float('inf')
MAX = 500 + 5

n = int(input())
graph = [[] for _ in range(MAX)]
dist = [ptive_inf] * MAX

def dijkstra(u):
    pq = queue.PriorityQueue()
    dist[u] = 0
    pq.put(Node(u, 0))
    
    while not pq.empty():
        node = pq.get()
        for new_node in graph[node.b]:
            v = new_node.b
            w = new_node.w
            if w + node.w < dist[v]:
                dist[v] = w + node.w
                pq.put(Node(v, dist[v]))


for i in range(n):
    a, b, w = list(map(int, input().split()))
    graph[a].append(Node(b, w))
    graph[b].append(Node(a, w))

u = int(input())
dijkstra(u)

q = int(input())

for i in range(q):
    v = int(input())
    if dist[v] != ptive_inf:
        print(dist[v])
    else:
        print("NO PATH")

    