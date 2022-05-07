import math    

testcase = int(input())
for idx in range(1, testcase + 1):
    second = int(input())
    root = math.ceil(math.sqrt(second))
    temp = root * root - second
    if temp < root:
        row = root
        column = temp + 1
    else:
        column = root
        row = second - (root-1) *(root-1)
    if not root % 2:
        temp = column
        column = row
        row = temp
    print(f"Case {idx}: {column} {row}")
