def binary_search(arr, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return True
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

ans = 0
j = 0
for i in range(n): 
    while j < i and  arr[i] - arr[j] > k:
        j += 1
    if arr[i] - arr[j] == k:
        ans += 1
print(ans)
