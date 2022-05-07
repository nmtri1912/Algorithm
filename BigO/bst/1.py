testcase = int(input())

for _ in range(testcase):
    n, x = map(int, input().split())
    s = set()
    
    arr = list(map(int, input().split()))
    
    for e in arr:
        s.add(e)
        
    lenng = len(s)
    if lenng == x:
        print("Good");
    elif lenng < x:
        print("Bad")
    else:
        print("Average")
