n = int(input())

s = dict()
for i in range(n):
    name = input()
    if name in s:
        s[name] = s[name] + 1
    else:
        s[name] = 1
ans = ""
max = 0
for key, value in s.items():
    if value > max:
        max = value
        ans = key
print(ans)
