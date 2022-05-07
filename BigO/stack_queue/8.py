def main():
    n = int(input())
    ans = []
        
    for _ in range(n):
        
        str = input()
        top = 0
        tem_cnt = 0
        cnt = 0
        for ch in str:
            if ch == '<':
                top+=1
            else:
                top-=1
                if top < 0:
                    break
                tem_cnt+=1
                if top == 0:
                    cnt = tem_cnt
        ans.append(cnt*2)
    
    for an in ans:
        print(an)

if __name__== "__main__":
    main()
