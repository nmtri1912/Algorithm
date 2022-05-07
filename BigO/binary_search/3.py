def binary_search(arr, n, x):
    low = 0
    high = arr[n-1]
    
    while low < high:
        mid = low + (high - low + 1) // 2
        count = 0
        for i in range(n):
            if arr[i] > mid:
                count = count + arr[i] - mid
        if count >= x:
            low = mid
        else:
            high = mid - 1
    return low

N , M = list(map(int, input().split()))

arr = list(map(int, input().split()))

arr.sort()

ans = binary_search(arr, N, M)

print(ans)