INF = (1 << 30) * 100 + 7

def bellman_ford(s):
   dist[s][s] = 0

   for i in range(n - 1):
      for edge in graph:
         u, v, w = edge
         if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
            dist[s][v] = dist[s][u] + w

   for i in range(n - 1):
      for edge in graph:
         u, v, w = edge
         if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
            dist[s][v] = -INF

tc = 1
while True:
   n = int(input())
   if n == 0:
      break

   monuments = []
   graph = []
   dist = [[INF] * n for _ in range(n)]

   for i in range(n):
      name, *weights = input().split()
      monuments.append(name)
      for j in range(n):
         w = int(weights[j])
         if i != j and w == 0:
            continue
         if i == j and w >= 0:
            w = 0
         graph.append((i, j, w))

   for i in range(n):
      bellman_ford(i)

   print('Case #{}:'.format(tc))
   tc += 1
   q = int(input())

   for _ in range(q):
      u, v = map(int, input().split())
      if dist[u][v] <= -INF:
         print('NEGATIVE CYCLE')
      else:
         print('{}-{} {}'.format(monuments[u], monuments[v], 'NOT REACHABLE' if dist[u][v] == INF else dist[u][v]))