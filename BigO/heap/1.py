import queue

n = int(input())
a = list(map(int, input().split()))
pq = queue.PriorityQueue()

for i in range(n):
	pq.put(-a[i])

	if i < 2:
		print(-1)
	else:
		first = -pq.get()
		second = -pq.get()
		third = -pq.get()

		print(first * second * third)

		pq.put(-first)
		pq.put(-second)
		pq.put(-third)