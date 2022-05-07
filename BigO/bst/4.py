testcase = int(input())

for _ in range(testcase):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    s = set()
    
    for i in range(n):
        s.add(arr[i])
    for i in range(n,n+m):
        if arr[i] in s:
            print("YES")
        else:
            print("NO")
        s.add(arr[i])