def check(n, t, arr):
    l = 0
    r = 0
    cnt = 0
    sum = 0
    
    while (r < n):
        sum+=arr[r]
        r+=1
        while sum > t:
            sum-=arr[l]
            l+=1
        cnt = max(cnt,r-l)
        
    return cnt

            
def main():
    n_k = list(map(int, input().split()))
    n = n_k[0]
    t = n_k[1]
    arr = list(map(int, input().split()))
    
    result = check(n, t, arr)
    print(result)

if __name__== "__main__":
    main()

