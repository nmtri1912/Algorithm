def binary_search(arr, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x and (mid == left or arr[mid-1] != x):
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

test = 1
while True:
    N, Q = list(map(int, input().split()))
    if N == Q == 0:
        break
    arr = []
    for i in range(N):
        arr.append(int(input()))
    
    arr.sort()
    print(f"CASE# {test}:")
    test+=1
    for i in range(Q):
        x = int(input())
        idx = binary_search(arr, 0, N - 1, x)
        if idx == -1:
            print(f"{x} not found")
        else:
            print(f"{x} found at {idx+1}")
            