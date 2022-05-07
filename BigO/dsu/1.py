def find(x):
    while x != parent[x]:
        x = parent[x]
    return x    

def union_set(a, b):
    pa = find(a)
    pb = find(b)
    if pa == pb:
        return
    if rank[pa] > rank[pb]:
        parent[pb] = pa
        num[pa] += num[pb]
    elif rank[pa] < rank[pb]:
        parent[pa] = pb
        num[pb] += num[pa]
    else:
        parent[pa] = pb
        num[pb] += num[pa]
        rank[pb]+=1
        

testcase = int(input())

for _ in range(testcase):
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    num = [1] * (n+1)
    rank = [0] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        union_set(a, b)
        
    res = 0
    for i in range(1, n+1):
        if parent[i] == i and num[i] > res:
            res = num[i]
    print(res)