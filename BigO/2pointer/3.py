def check(n, m, min_diff_size, max_diff_size, arr1, arr2):
    i=0 
    j=0
    cnt=0
    ans = {}
    while i < n and j < m:
        if arr2[j] >= arr1[i] - min_diff_size and arr2[j] <= arr1[i] + max_diff_size:
            ans.update({i+1:j+1})
            cnt+=1
            i+=1
            j+=1
        elif arr2[j] < arr1[i]:
            j+=1
        else:
            i+=1
            
    print(cnt)
    for k, v in ans.items():
        print(f"{k} {v}")
            
def main():
    n_k = list(map(int, input().split()))
    n = n_k[0]
    t = n_k[1]
    min_diff_size = n_k[2]
    max_diff_size = n_k[3]
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    check(n, t, min_diff_size, max_diff_size, arr1, arr2)

if __name__== "__main__":
    main()
