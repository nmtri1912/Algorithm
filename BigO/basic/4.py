def check(s1, s2):
    for i in range(len(s1) - 1, -1, -1):
        if s1[i] != 'z':
            s1 = s1[:i] + chr(ord(s1[i]) + 1) + s1[i+1:]
            break
        else:
            s1 = s1[:i] + 'a' + s1[i+1:]
    
    if s1 != s2:
        return s1
    else:
        return 'No such string'
        
def main():
    s1 = input()
    s2 = input()
    
    result = check(s1, s2)
    print(result)

if __name__== "__main__":
    main()

