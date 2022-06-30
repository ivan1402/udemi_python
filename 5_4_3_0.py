# -5.67 3.5 6.89 -3.0

l = input().split()
for x, y in enumerate(l):
    if float(l[x]) < 0:
        l[x] = -1.0
print(*l)
