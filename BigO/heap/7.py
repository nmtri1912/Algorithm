import queue
s = []
q = queue.Queue()
pq = queue.PriorityQueue()
 
while True:
    try:
        n = int(input())
    except EOFError:
        break
 
    s.clear()
    q.queue.clear()
    pq.queue.clear()    
    is_stack = is_queue = is_pq = True
     
    for _ in range(n):
        type, x = map(int, input().split())
        if type == 1:
            s.append(x)
            q.put(x)
            pq.put(-x)
        else:
            if len(s) == 0:
                is_stack = is_queue = is_pq = False
            else:
                if x != s.pop():
                    is_stack = False
                if x != q.get():
                    is_queue = False
                if x != -pq.get():
                    is_pq = False
 
    if is_stack + is_queue + is_pq == 0:
        print("impossible")
    elif is_stack + is_queue + is_pq > 1:
        print("not sure")
    elif is_stack:
        print("stack")
    elif is_queue:
        print("queue")
    else:
        print("priority queue")