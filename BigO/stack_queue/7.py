from queue import Queue

class Task:
    def __init__(self, t, d, f):
        self.t = t
        self.d = d
        self.f = f

def main():
    n, m = list(map(int, input().split()))
    
    tasks = []
    for _ in range(n):
        t, d = list(map(int, input().split()))
        tasks.append(Task(t, d, 0))

    queue = Queue()
    t = tasks[0].t + tasks[0].d
    tasks[0].f = t
    queue.put(t)
    
    for i in range(1, n):
        while queue.qsize() > 0 and tasks[i].t >= queue.queue[0]:
            queue.get()
        
        if t <= tasks[i].t:
            t = tasks[i].t + tasks[i].d
            tasks[i].f = t
            queue.put(t)
        else:
            if queue.qsize() > m:
                tasks[i].f = -1
            else:
                t += tasks[i].d
                tasks[i].f = t
                queue.put(t)
    
    ans = []
    for i in range(n):
        ans.append(str(tasks[i].f))
    print(' '.join(ans))
    
if __name__== "__main__":
    main()

