def check(n, arr):
    idx = n
    cnt=0
    for i in range(n-1, -1, -1):
        if i < idx:
            cnt+=1
        idx = min(idx,i-arr[i])
    
    print(cnt)
    
def main():
    n = int(input())
    arr = list(map(int, input().split()))    
    check(n, arr)

if __name__== "__main__":
    main()

