def check(n, m, arr1, arr2):
    need=0 
    pre=0
    while need < n and pre < m:
        if arr2[pre] >= arr1[need]:
            need+=1
        pre+=1
        
    print(n - need)
            
def main():
    n_k = list(map(int, input().split()))
    n = n_k[0]
    t = n_k[1]
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    check(n, t, arr1, arr2)

if __name__== "__main__":
    main()

