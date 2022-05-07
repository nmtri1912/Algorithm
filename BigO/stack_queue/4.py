def main():
    dim, queries = list(map(int, input().split()))
    result = []

    while dim and queries:
        queue = []
        for i in range(min(dim, 1000)):
            queue.append(i+1)
        ans = []
        for i in range(queries):
            inp = input()
            if inp == 'N':
                tmp = queue.pop(0)
                ans.append(tmp)
                queue.append(tmp)
            else:
                idx = int(inp.split()[1])
                tmp_queue = []
                idx = int(inp.split()[1])
                tmp_queue.append(idx)
                while len(queue):
                    e = queue.pop(0)
                    if e != idx:
                        tmp_queue.append(e)
                    
                queue = tmp_queue
        result.append(ans)
        
        dim, queries = list(map(int, input().split()))
    
    for idx, val in enumerate(result, 1):
        print(f"Case {idx}:")
        for e in val:
            print(e)
        
if __name__== "__main__":
    main()
