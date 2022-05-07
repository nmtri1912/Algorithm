class Node:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def __lt__(self, other):
        return self.first < other.first


n = int(input())
arr = list(map(int, input().split()))
pair_list = []
for i in range(len(arr)):
    pair_list.append(Node(arr[i], i))
    
pair_list.sort()

ans = 0
for i in range(n - 1):
    if pair_list[i].first == pair_list[i+1].first:
        ans+=1
    if ans == 2:
        print("YES")
        line = []
        for j in range(n):
            line.append(str(pair_list[j].second + 1))
        print(' '.join(line))
            
        for j in range(n-1):
            line = []
            if pair_list[j].first == pair_list[j+1].first:
                ans+=1
                pair_list[j].second, pair_list[j+1].second = pair_list[j+1].second, pair_list[j].second
                for k in range(n):
                    line.append(str(pair_list[k].second + 1))
                print(' '.join(line))
                pair_list[j].second, pair_list[j+1].second = pair_list[j+1].second, pair_list[j].second
                if ans == 2:
                    exit()
print("NO")