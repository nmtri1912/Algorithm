def binary_search_lower(arr, left, right, x):
    res = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < x:
            res = arr[mid]
            left = mid + 1
        else:
            right = mid - 1
    return res

def binary_search_higher(arr, left, right, x):
    res = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > x:
            res = arr[mid]
            right = mid - 1
        else:
            left = mid + 1
    return res


N = int(input())

arr = list(map(int, input().split()))

Q = int(input())

query = list(map(int, input().split()))
for i in query:
    ans1 = binary_search_lower(arr, 0, N-1, i)
    ans2 = binary_search_higher(arr, 0, N-1, i)
    if ans1 == -1:
        ans1 = 'X'
    if ans2 == -1:
        ans2 = 'X'
    print(f"{ans1} {ans2}")