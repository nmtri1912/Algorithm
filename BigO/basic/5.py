def check(k1, k2, arr1, arr2):
    if arr1[k1-1] < arr2[-k2]:
        return True
    return False
            
def main():
    n_list = list(map(int ,input().split()))
    n1 = n_list[0]
    n2 = n_list[1]
    
    k_list = list(map(int, input().split()))
    k1 = k_list[0]
    k2 = k_list[1]
    
    arr1 = list(map(int ,input().split()))
    arr2 = list(map(int ,input().split()))
    
    result = check(k1, k2, arr1, arr2)
    if result:
        print("YES")
    else:
        print("NO")

if __name__== "__main__":
    main()

