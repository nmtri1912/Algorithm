import queue

class Printer:
    def __init__(self, i, p):
        self.i = i
        self.p = p
    
    def __lt__(self, other):
        return self.p > other.p

pq = queue.PriorityQueue()
q = queue.Queue()

test_case = int(input())

for _ in range(test_case):
    q.queue.clear()
    pq.queue.clear()
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    for i in range(n):
        p = arr[i]
        s = Printer(i, p)
        q.put(s)
        pq.put(s)
    
    ans = 0
    while True:
        if q.queue[0].p == pq.queue[0].p:
            if q.queue[0].i == m:
                break
            q.get()
            pq.get()
            ans+=1
        else:
            q.put(q.get())
    print(ans+1)
