INF = float('inf')

T = int(input())

for i in range(T):
    graph = []
    first_line = input()
    M = len(first_line)
    graph.append(first_line)
    for j in range(M -1):
        line = input()
        graph.append(line)
        
    dist = [[INF for i in range(M)] for j in range(M)]
    for i in range(M):
        for j in range(M):
            if graph[i][j] == 'Y':
                dist[i][j] = 1
            if i == j:
                dist[i][j] = 0
    
    def Floyd(dist):
        for k in range(M):
            for i in range(M):
                if dist[i][k] == INF:
                    continue
                for j in range(M):
                    if dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    
    Floyd(dist)
    id = 0
    max_friends = 0
    for i in range(M):
        count = 0
        for j in range(M):
            if dist[i][j] == 2:
                count+=1
        if count > max_friends:
            max_friends = count
            id = i
    print(id, max_friends)
