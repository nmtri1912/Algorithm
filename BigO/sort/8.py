def check(p):    
    p.sort(key=lambda k: (k.x, k.y))
    
    if p[0].x == p[1].x and p[1].x == p[2].x and p[2].x != p[3].x and p[3].x == p[4].x and p[4].x != p[5].x and p[5].x == p[6].x and p[6].x == p[7].x and p[0].y == p[3].y and p[3].y == p[5].y and p[5].y != p[1].y and p[1].y == p[6].y and p[6].y != p[2].y and p[2].y == p[4].y and p[4].y == p[7].y:
        print('respectable')
    else:
        print('ugly')
    
class Point():
    def __init__(self, a, b):
        self.x = a
        self.y = b
    
def main():
    a = []
    b = []
    
    points = []
    
    for i in range(8):
        k_v = list(map(int, input().split()))
        p = Point(k_v[0], k_v[1])
        points.append(p)
    result = check(points)
    
if __name__== "__main__":
    main()

