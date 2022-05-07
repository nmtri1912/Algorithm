def check(n, arr):
    if n == 1:
        if arr[0] > 15:
            return 15
        else:
            return arr[0] + 15
    
    if arr[0] > 15:
        return 15
    
    result = 0
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] > 15:
            result = arr[i] + 15
        else:
            result = arr[i+1] + 15
    if result > 90:
        result = 90
        
    return result
        
            
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = check(n, arr)
    print(result)

if __name__== "__main__":
    main()

