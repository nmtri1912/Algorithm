def check(string):
    count = 0
    for i in range(len(string)-1):
        diff = abs(ord(string[i+1]) - ord(string[i]))
        if diff > 13:
            diff = 26 - diff
        count += diff
    return count
            
def main():
    string = input()
    string = 'a' + string
    
    result = check(string)
    print(result)

if __name__== "__main__":
    main()

