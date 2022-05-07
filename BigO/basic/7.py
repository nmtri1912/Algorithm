def check(k, dict_len, pwd):
    count = 0
    for i in range(len(pwd)):
        count += dict_len.get(i, 0)
    print(count)
    2 + 2//100 + 1
    min = count + count // k * 5 + 1
            
    count = -1 #include len = 0
    for i in range(len(pwd) + 1):
        count += dict_len.get(i, 0)
    print(count)
    max = count + count//k * 5 + 1
    
    print(f"{min} {max}")
    
    
def main():
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]
    
    dict_len = {}
    for i in range(n):
        pwd = input()
        dict_len.setdefault(len(pwd), 0)
        dict_len[len(pwd)] += 1
    
    pwd = input()    
    
    check(k, dict_len, pwd)

if __name__== "__main__":
    main()

