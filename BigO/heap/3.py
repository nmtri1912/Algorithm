import queue
pq = queue.PriorityQueue()

while True:
    n = int(input())
    
    if n == 0:
        break

    for x in input().split():
        pq.put(int(x))
    
    ans = 0
    
    while pq.qsize() > 1:
        a = pq.get()
        b = pq.get()
        ans += a + b
        pq.put(a + b)

    print(ans)
    pq.get()