import queue
 
def bfs(graph, src, rank):
    q = queue.Queue()
    rank[src] = 0
    q.put(src)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if rank[v] == 'undefined':
                rank[v] = rank[u] + 1
                q.put(v)
    return rank
 
n = int(input())
S = dict()
cnt = 0
graph = []
for i in range(n):
    line = input().split()
    v = []
    for name in line:
        if name in S:
            id = S[name]
        else:
            S[name] = cnt
            id = cnt
            graph.append([])
            cnt+= 1
        v.append(id)
    for x in v:
        for y in v:
            if x != y:
                graph[x].append(y)
rank = ['undefined' for i in range(cnt)]
if 'Isenbaev' in S:
    rank = bfs(graph, S['Isenbaev'], rank)
a = []
for name in S:
    a.append(name)
a.sort()
for name in a:
    print(name + ' ' + str(rank[S[name]]))
