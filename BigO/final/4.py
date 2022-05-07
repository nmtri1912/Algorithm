import math
import queue
INF = 10 ** 9

def cal_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2))

def prim(N):
    visited = [False] * (N + 1)
    dist = [INF] * (N + 1)
    sum = 0
    



testcase = int(input())
dist = [[0 for _ in range(105)] for _ in range(105)]
x = [0] * 105
y = [0] * 105

for _ in range(testcase):
    breakline = input()
    n = int(input())

    for i in range(n):
        x[i], y[i] = map(float, input().split())

    for i in range(n):
        for j in range(i+1,n):
            dist[i][j] = dist[j][i] = cal_distance(x[i], y[i], x[j], y[j])
    