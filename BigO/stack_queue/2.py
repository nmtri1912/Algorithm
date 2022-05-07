def check(stack_in, n):
    if n == 1 or n == 2 or n == 3:
        return True
    
    stack_out = []
    current = 1
    
    while len(stack_in) and current != n+1:
        if stack_in[-1] == current:
            current+=1
            stack_in.pop()
        elif len(stack_out) and stack_out[-1] == current:
            stack_out.pop()
            current+=1
        else:
            stack_out.append(stack_in[-1])
            stack_in.pop()
            
    while len(stack_out):
        if current == stack_out[-1]:
            stack_out.pop()
            current+=1
        else:
            return False
        
    return True


def main():
    
    n = int(input())
    ans = []
    while n:
        arr = list(map(int, input().split()))
        
        arr.reverse()
        
        result = check(arr, n)
        if result:
            ans.append("yes")
        else:
            ans.append("no")
        
        n = int(input())
        
    for an in ans:
        print(an)

if __name__== "__main__":
    main()

