def main():
    val = {
        'C': 12,
        'H': 1,
        'O': 16,
        '(': -1,
        ')': 0
    }
    formula = input()
    stack = []
        
    for e in formula:
        if e == '(':
            stack.append(val['('])
        elif e == ')':
            k = val[')']
            total = 0
            while k != val['(']:
                k = stack.pop()
                if k != val['(']:
                    total += k
            stack.append(total)
        elif e in ['C', 'H', 'O']:
            stack.append(val[e])
        else: #2-9
            k = stack.pop()
            stack.append(k * int(e));
    
    result = 0
    while len(stack) > 0:
        result += stack.pop()
    
    print(result)
            

if __name__== "__main__":
    main()
