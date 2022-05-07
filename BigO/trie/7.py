class Node:
    def __init__(self):
        self.child = dict()
        self.is_vulnerable = False

def add_word(root, s):
    flag = False
    temp = root
    for ch in s:
        if ch not in temp.child:
            flag = True
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if temp.is_vulnerable:
            return False
    temp.is_vulnerable = True
    return flag

n = int(input())
root = Node()
vulnerable = True
for i in range(n):
    s = input()
    vulnerable &= add_word(root, s)
print("non vulnerable" if vulnerable else "vulnerable")