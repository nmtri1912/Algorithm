import queue


taken = [False] * 1000005
max_heap = queue.PriorityQueue()
min_heap = queue.PriorityQueue()
money = 0
nbills = 0

n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    
    for x in a[1:]:
        nbills += 1
        max_heap.put((-x, nbills))
        min_heap.put((x, nbills))

    while taken[max_heap.queue[0][1]]:
        max_heap.get()
    
    while taken[min_heap.queue[0][1]]:
        min_heap.get()
    
    taken[max_heap.queue[0][1]] = taken[min_heap.queue[0][1]] = True
    money += -max_heap.get()[0] - min_heap.get()[0]

print(money)

