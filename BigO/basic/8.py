

# def automaton(a, b):
#     index = 0
#     string = ''
#     for i in range(len(a)):
#         if index == len(b):
#             break
#         if a[i] == b[index]:
#             string+=a[i]
#             index+=1
#     return string == b

# def array(a, b):
#     a = ''.join(sorted(a))
#     b = ''.join(sorted(b))
#     return a == b

# def both(a, b):
#     for i in range(len(b)):
#         index = a.find(b[i])
#         if index == -1:
#             return False
#         a = a[:index] + a[index+1:] 
#     return True
            
        
def main():
    s = input()
    t = input()
    
    cnt_s, cnt_t = [0] * 26
    
    for e in cnt_s:
        idx = ord(e) - ord('a')
        cnt_s[idx] += 1
        
    for e in cnt_t:
        idx = ord(e) - ord('a')
        cnt_t[idx] += 1
    
    need_tree, automaton, array = False
    
    for i in range(0, 26):
        if cnt_t[i] > cnt_s[i]:
            need_tree = True
        if cnt_t[i] < cnt_s[i]:
            automaton = True
        
        
            
    if need_tree:
        print('need tree')
    elif automaton and array:
        print('both')
    elif automaton:
        print('automaton')
    else:
        print('array')
        
        

    # if automaton(a, b):
    #     print('automaton')
    # elif array(a, b):
    #     print('array')
    # elif both(a, b):
    #     print('both')
    # else:
    #     print('need tree')

if __name__== "__main__":
    main()
