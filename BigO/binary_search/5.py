def is_possible(arr, n, k):
    for i in range(1, n):
        diff = arr[i] - arr[i-1]
        if diff == k:
            k-=1
        elif diff > k:
            return False
    return True

def binary_search(arr, n):
    left = 1
    right = 10000000
    result = 0
    while left <= right:
        mid = left + (right - left) // 2
        if is_possible(arr, n, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

testcase = int(input())

for i in range(testcase):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [0] + arr
    ans = binary_search(arr, n+1)
    print(f"Case {i+1}:", ans)