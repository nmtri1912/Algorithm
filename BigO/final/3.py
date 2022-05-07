def find(x):
    while x != parent[x]:
        x = parent[x]
    return x    

def union_set(a, b, ans):
    pa = find(a)
    pb = find(b)
    if pa == pb:
        return ans
    ans-=1
    if rank[pa] > rank[pb]:
        parent[pb] = pa
    elif rank[pa] < rank[pb]:
        parent[pa] = pb
    else:
        parent[pa] = pb
        rank[pb]+=1
    return ans

n, m = map(int, input().split())
idx = 1
global ans
while m and n:
    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)
    ans = n
    
    for _ in range(m):
        i, j = map(int, input().split())
        ans = union_set(i, j, ans)
    print(f"Case {idx}: {ans}")
    idx+=1
    
    n, m = map(int, input().split())
    