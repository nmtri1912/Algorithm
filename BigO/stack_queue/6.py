from queue import Queue

class Car:
    def __init__(self, id, arrive_time):
        self.id = id
        self.arrive_time = arrive_time
        
def main():
    testcase = int(input())
    result = []
    
    for k in range(testcase):
        n, t , m = list(map(int, input().split()))
        q = [Queue(), Queue()] # 0: left, 1: right
        for i in range(m):
            arrive_time, bank = input().split()
            if bank == 'left':
                q[0].put(Car(i, int(arrive_time)))
            else:
                q[1].put(Car(i, int(arrive_time)))
                
        cur_time = 0
        next_time = 0
        cur_side = 0 # 0: left, 1: right
        answer = [0] * m
        
        waiting = (not q[0].empty()) + (not q[1].empty())
        # print("waiting", waiting)
        
        while waiting:
            if waiting == 1:
                if q[0].empty():
                    next_time = q[1].queue[0].arrive_time
                else:
                    next_time = q[0].queue[0].arrive_time
            else:
                next_time = min(q[0].queue[0].arrive_time, q[1].queue[0].arrive_time)
            cur_time = max(cur_time, next_time)
            
            loaded = 0
            while not q[cur_side].empty():
                car = q[cur_side].queue[0]
                if car.arrive_time <= cur_time and loaded < n:
                    loaded += 1
                    q[cur_side].get()
                    answer[car.id] = cur_time + t
                else:
                    break
            cur_time+=t
            cur_side = 1-cur_side
            waiting = (not q[0].empty()) + (not q[1].empty())
        for e in answer:
            print(e)
        
        if k < testcase - 1:
            print()
        
if __name__== "__main__":
    main()
