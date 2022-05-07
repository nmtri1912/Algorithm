from queue import Queue

def main():
    n = int(input())
    sum_ans = []
    sum_cnt = []
    queue = Queue()
    
    while n:
        for i in range(n):
            queue.put(i+1)
        ans = []
        
        while queue.qsize() > 1:
            ans.append(str(queue.get()))
            x = str(queue.get())
            queue.put(x)
        
        ans = ', '.join(ans)
        sum_ans.append(ans)
        sum_cnt.append(str(queue.get()))
        
        n = int(input())

    for i in range(len(sum_cnt)):
        ans_1 = "Discarded cards: " + sum_ans[i]
        ans_2 = "Remaining card: " + sum_cnt[i]
        print(ans_1.strip())
        print(ans_2.strip())
    
if __name__== "__main__":
    main()
