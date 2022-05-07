def binary_search(arr, left, right, x, cur):
    while left <= right:
        mid = left + (right - left) // 2
        if x == arr[mid] and mid != cur:
            return 1
        elif x > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return 0

t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    for i in range(n):
        ans += binary_search(arr, i, n-1, m-arr[i], i)
        
    print(ans)