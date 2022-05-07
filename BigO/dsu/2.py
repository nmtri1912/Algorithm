def find(u):
    while u != parent[u]:
        u = parent[u]
    return u

def union_set(u, v):
    pu = find(u)
    pv = find(v)
    
    if pu == pv:
        return
    if rank[pu] > rank[pv]:
        parent[pv] = pu
    elif rank[pu] < rank[pv]:
        parent[pu] = pv
    else:
        parent[pu] = pv
        rank[pv]+=1


testcase = int(input())

for _ in range(testcase):
    input()
    p, t = map(int, input().split())
    parent = [i for i in range(p+1)]
    tree = [set() for _ in range(p+1)]
    rank = [0] * (p + 1)
    line = 'start'
    while not EOFError or line:
        i, j = map(int, input().split())
        tree[i].add(j)
    
    for i in range(0, p-1):
        for j in range(i+1, p):
            if tree[i] == tree[j]:
                union_set(i, j)
    ans = -1
    for i in range(p):
        if i == parent[i]:
            ans+=1
    print(ans)
    print()
