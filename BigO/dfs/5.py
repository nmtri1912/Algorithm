import sys
sys.setrecursionlimit(10**6)

def DFS(i, visited, n):
    global n_boms
    visited[i] = True
    for u in graph[i]:
        if not visited[u]:
            n_boms+=1
            DFS(u, visited, n)

n, m = list(map(int ,input().split()))

graph = [[] for _ in range(10005)]

for i in range(m):
    u, v = list(map(int, input().split()))
    graph[u].append(v)

res = []
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    if not visited[i]:
        n_boms = 1
        DFS(i, visited, n)
        res.append(n_boms)
        if n_boms == n:
            break
        
print(max(res))