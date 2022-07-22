N = 6

a = [0] * N
for i in range(N):
    a[i] = i ** 2
print(a)


b = [i ** 2 for i in range(N)]
print(b)

c = [x for x in range(-5, 5) if x < 0]
print(c)