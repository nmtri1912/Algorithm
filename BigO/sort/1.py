def check(n, x, arr):
    sum = 0
    arr.sort()
    
    for i in range(n):
        sum += arr[i] * x
        if x > 1:
            x-=1
    
    return sum

            
def main():
    n_k = list(map(int, input().split()))
    n = n_k[0]
    x = n_k[1]
    arr = list(map(int, input().split()))
    
    result = check(n, x, arr)
    print(result)

if __name__== "__main__":
    main()

