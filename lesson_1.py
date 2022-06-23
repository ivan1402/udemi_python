n = int(input())
s = 0
for i in range(0, n):
    if i % 3 == 0 or i % 5 == 0:
        s += i
    else:
        continue
print(s)
