def check(arr_l ,arr_r):
    l_min = min(arr_l)
    r_max = max(arr_r)
    for i in range(len(arr_l)):
        if arr_l[i] == l_min and arr_r[i] == r_max:
            return i+1
    return -1
            
        
def main():
    n = int(input())
    
    arr_l = []
    arr_r = []
    for i in range(n):
        lr = list(map(int, input().split()))
        arr_l.append(lr[0])
        arr_r.append(lr[1])
        
    result = check(arr_l, arr_r)
    print(result)

if __name__== "__main__":
    main()
