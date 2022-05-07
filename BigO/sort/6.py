def check(n, arr):
    pre = [0] * (1000 + 5)
    ans = []
    max_len = 0
    for i in range(n):
        if pre[arr[i]] == 0:
            ans.append(arr[i])
        pre[arr[i]]+=1
        max_len = max(max_len, pre[arr[i]])
    
    print(f"{max_len} {len(ans)}")
    
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    check(n, arr)

if __name__== "__main__":
    main()


