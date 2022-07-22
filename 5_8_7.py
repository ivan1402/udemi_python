# 8.5 11.3 1.0 -4.5 11.34 6.45
a = input().split()
b = [i for i in a[::2]]
print(*b)