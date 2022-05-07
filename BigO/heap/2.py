import queue

pq = queue.PriorityQueue()
pq_remove = queue.PriorityQueue()

query = int(input())
for i in range(query):
    line = list(map(int, input().split()))
    if line[0] == 1:
        pq.put(line[1])
    elif line[0] == 2:
        pq_remove.put(line[1])
    else:
        while not pq_remove.empty() and pq.queue[0] == pq_remove.queue[0]:
            pq.get()
            pq_remove.get()
        print(pq.queue[0])
