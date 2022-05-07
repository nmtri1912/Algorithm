from queue import Queue

def BFS(key, dist, des_key, arr):
    q = Queue()
    q.put(key)
    dist[key] = 0
    while not q.empty():
        u = q.get()
        for i in range(len(arr)):
            merge_key = (u * arr[i]) % 100000
            if dist[merge_key] == -1:
                dist[merge_key] = dist[u] + 1
                if merge_key == des_key:
                    return dist[merge_key]
                q.put(merge_key)
    return -1
def main():
    MAX = 100000 + 1
    dist = [-1] * MAX
    key, des_key = list(map(int, input().split()))
    n = int(input())
    arr = list(map(int, input().split()))
    
    ans = BFS(key, dist, des_key, arr)
    print(ans)

if __name__== "__main__":
    main()