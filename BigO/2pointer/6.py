def check(n, arr):
    fre = [0] * (10**6)
    diff = 0
    l = 0
    max_len = 0
    r = 0
    
    for r in range(n):
        if fre[arr[r]] == 0:
            diff+=1
        fre[arr[r]]+=1
        if diff > 2:
            max_len = max(max_len, r - 1 - l)
            if fre[arr[l]] == 1:
                diff-=1
            fre[arr[l]]-=1
            l+=1
        else:
            max_len+=1

    print(max_len)
    
    
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    check(n, arr)

if __name__== "__main__":
    main()

