import queue
top3 = queue.PriorityQueue()
rest = queue.PriorityQueue()
nreviews = 0

n = int(input())

for _ in range(n):
    line = list(map(int, input().split()))
    type = line[0]
    
    if type == 1:
        x = line[1]
        nreviews += 1

        if not top3.empty() and top3.queue[0] < x:
            rest.put(-top3.get())
            top3.put(x)
        else:
            rest.put(-x)

        if nreviews % 3 == 0:
            top3.put(-rest.get())
    else:
        if top3.empty():
            print("No reviews yet")
        else:
            print(top3.queue[0])