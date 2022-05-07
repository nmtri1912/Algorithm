
def check(n, arr):
    i = 0
    j = n - 1
    cnt_a = 0
    cnt_b = 0
    
    a = 0
    b = 0
    
    while True:
        if a <= b:
            a+=arr[i]
            i+=1
            cnt_a+=1
        else:
            b+=arr[j]
            j -= 1
            cnt_b+=1
            
        if i > j:
            break
        
    print(f"{cnt_a} {cnt_b}")
    
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    check(n, arr)

if __name__== "__main__":
    main()

