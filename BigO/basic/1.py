def check(arr):
    if len(arr) == 1:
        if arr[0]:
            return True
        return False
    count = 0
    for e in arr:
        if e == 0:
            count += 1
    if count != 1:
        return False
    return True
            
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = check(arr)
    if result:
        print("YES")
    else:
        print("NO")

if __name__== "__main__":
    main()

