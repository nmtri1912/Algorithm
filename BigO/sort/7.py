def check(n, arr):
    sum = 0
    cnt = 0;
    
    if n == 0:
        return 0

    arr.sort(reverse=True)
    for i in range(len(arr)):
        sum += arr[i]
        cnt+=1
        if sum >= n:
            break
    if sum < n:
        return -1
    else:
        return cnt
    
    
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = check(n, arr)
    print(result)

if __name__== "__main__":
    main()

