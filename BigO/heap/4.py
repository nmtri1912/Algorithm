import queue

class Post:
    def __init__(self, _id, _old_score, _new_score):
        self.id = _id
        self.old_score = _old_score
        self.new_score = _new_score
        self.diff = self.new_score - self.old_score
    
    def __lt__(self, other):
        return self.diff > other.diff or (self.diff == other.diff and self.id > other.id)

n = int(input())
pq = queue.PriorityQueue()

for _ in range(n):
    id, old_score, post, like, comment, share = map(int, input().split())
    new_score = post * 50 + like * 5 + comment * 10 + share * 20
    pq.put(Post(id, old_score, new_score))

for i in range(5):
    t = pq.get()
    print(t.id, t.new_score)