def check(n, x,arr):
    arr.sort()
    a = arr[0];
    b = arr[n] / 2;
    m = min(a,b)
    ans=min(m * n + m * 2 * n, x);

    print(ans)
    
def main():
    n_k = list(map(int, input().split()))
    n = n_k[0]
    x = n_k[1]
    arr = list(map(int, input().split()))
    
    check(n, x, arr)

if __name__== "__main__":
    main()

