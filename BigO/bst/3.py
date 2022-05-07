import sys
import math
 
locations, peoples = map(int, input().split())
location = dict()
for i in range(locations):
    x, y, people = map(int, input().split())
    r = x * x + y * y
    if r in location:
        location[r] += people
    else:
        location[r] = people
radius = []
for r in location:
    radius.append(r)
radius.sort()
for r in radius:
    peoples += location[r]
    if peoples >= 1000000:
        print(math.sqrt(r))
        sys.exit()
    
print("-1")
     
