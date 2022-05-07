import math
from typing import Any

class Point:
    x: Any
    y: Any
    
    def __init__(self):
        pass
    
    def __call__(self, a, b):
        self.x = a
        self.y = b
        
    def get_distance(self, other):
        return math.sqrt((self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y))

n = int(input())
points = [Point()] * (n + 1)
print(points)
for i in range(n):
    x, y = map(float, input().split())
    print(x, y)
    points[i](x,y)
    
for point in points:
    print(f"{point.x}: {point.y}")
