def check(n, k, arr):
    fre = [0] * (10**6)
    diff = 0
    l = 0
    r = 0
    
    while r < n:
        if fre[arr[r]] == 0:
            diff+=1
        fre[arr[r]]+=1
        if diff == k:
            break
        r+=1

    diff_cnt = diff
    
    if diff_cnt == k:
        l = 1
        for l in range(n):
            if fre[arr[l]] == 1:
                diff-=1
            fre[arr[l]]-=1
            if diff < k:
                print(f"{l+1} {r+1}")
                break
        
    if diff_cnt < k:
        print("-1 -1")
    
def main():
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]
    arr = list(map(int, input().split()))
    
    check(n, k, arr)

if __name__== "__main__":
    main()

