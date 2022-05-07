def main():
    n = int(input())
    
    ans = []
    idx = 0
    
    for _ in range(n):
        
        s = input()
        stack = []
        e = ''
        
        for i in s:
            if i.isalpha():
                e += i
            elif i == "+" or i == "-" or i == "*" or i == "/" or i == "%" or i == "^":
                stack.append(i)
            elif i == ")" :
                e += stack.pop()
        ans.append(e)
    
    for an in ans:
        print(an)

if __name__== "__main__":
    main()

