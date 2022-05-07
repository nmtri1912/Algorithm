def check(n, arr):
    i = 0
    j = 0
    sum1 = 0
    sum2 = 0
    p1 = 0
    p2 = n-1
    while i + j < n:
        if i <= j:
            if arr[p1] >= arr[p2]:
                sum1+=arr[p1]
                p1+=1
            else:
                sum1+=arr[p2]
                p2-=1
            i+=1
        else:
            if arr[p1] >= arr[p2]:
                sum2+=arr[p1]
                p1+=1
            else:
                sum2+=arr[p2]
                p2-=1
            j+=1
        
    print(f"{sum1} {sum2}")
    
def main():
    n = int(input())
    arr = list(map(int, input().split()))    
    check(n, arr)

if __name__== "__main__":
    main()
