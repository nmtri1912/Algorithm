n = int(input())
arr = list(map(int, input().split()))

arr.sort()
if len(arr) % 2 == 0:
    index = len(arr)//2
    ans = arr[index - 1] + arr[index]
    print(ans/2)
else:
    ans = arr[len(arr)//2]
    print(ans)
    
