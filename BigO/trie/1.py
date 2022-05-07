class Node:
    def __init__(self):
        self.child = dict()
        self.max_value = -1

def add_word(root, s, value):
    tmp = root
    for c in s:
        if c not in tmp.child:
            tmp.child[c] = Node()
        tmp = tmp.child[c]
        tmp.max_value = max(tmp.max_value, value)

def get_result(root, s):
    tmp = root
    for c in s:
        if c not in tmp.child:
            return -1
        tmp = tmp.child[c]
    return tmp.max_value

n, q = map(int, input().split())
root = Node()

for _ in range(n):
    value, pior = input().split()
    add_word(root, value, int(pior))

for _ in range(q):
    s = input()
    print(get_result(root, s))