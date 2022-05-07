n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

sum_energy = sum(arr)

left = 0
right = 1000
mid = 0
while right - left > 10 ** -7:
    
    mid = (left + right) / 2
    sum_transfer = 0
    for i in range(n):
        if arr[i] > mid:
            sum_transfer = sum_transfer + arr[i] - mid
    sum_lost = k/100 * sum_transfer
    if n*mid < sum_energy - sum_lost:
        left = mid
    else:
        right = mid
        
print(mid)
    