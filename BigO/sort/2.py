def check(n, x, t, arr):
    arr.sort()
    return arr[t] - arr[t-1]
            
def main():
    n_k = list(map(int, input().split()))
    n = n_k[0]
    x = n_k[1]
    t = n_k[2]
    arr = list(map(int, input().split()))
    
    result = check(n, x, t, arr)
    print(result)

if __name__== "__main__":
    main()

