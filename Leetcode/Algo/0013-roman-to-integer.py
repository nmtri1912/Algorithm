class Solution(object):
    def romanToInt(self, s):
        i = len(s)-1 
        temp = 0
        while i >= 0:
            
            if s[i] == "I":
                temp += 1 
            elif s[i] == "V":
                if s[i-1] == "I" and i:
                    temp += 4;
                    i -= 2
                    continue
                else:
                    temp += 5;
            elif s[i] == "X":
                if s[i-1] == "I" and i:
                    temp+=9
                    i -= 2
                    continue
                else:
                    temp+=10
            elif s[i] == "L":
                if s[i-1] == "X" and i:
                    temp+=40
                    i-=2
                    continue
                else:
                    temp+=50
            elif s[i]== "C":
                if s[i-1] == "X" and i:
                    temp+=90
                    i-=2
                    continue
                else:
                    temp+=100
            elif s[i] == "D":
                if s[i-1] == "C" and i:
                    temp+=400
                    i-=2
                    continue
                else:
                    temp+=500
            elif s[i] == "M":
                if s[i-1] == "C" and i:
                    temp+=900
                    i-=2
                    continue
                else:
                    temp+=1000
            i-=1 
        
        
        return temp
