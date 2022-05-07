def check(n, arr):
    ans = []
    for i in range(n):
        x = 0
        for j in range(n):
            if arr[i] < arr[j]:
                x+=1
        ans.append(str(x+1))
    print(' '.join(ans))
    
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    check(n, arr)

if __name__== "__main__":
    main()

