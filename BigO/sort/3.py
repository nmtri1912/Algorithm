def check(n, arr):
    l = 0
    r = 0
    flag = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            l = i
            break
    
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:
            r = i
            break
    
    arr[l: r+1] = list(reversed(arr[l: r+1]))
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            flag = 1
            break
    if flag:
        print('no')
    else:
        print('yes')
        print(f"{l+1} {r+1}")
            
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    check(n, arr)

if __name__== "__main__":
    main()
