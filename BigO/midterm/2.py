n = int(input())
s = input()

arr = [0] * 26
90-65
for i in s:
    if 65 <= ord(i) <= 90:
        arr[ord(i) - 65] = 1
    elif 97 <= ord(i) <= 122:
        arr[ord(i) - 97] = 1

ans = min(arr)

if ans:
    print("YES")
else:
    print("NO")
    