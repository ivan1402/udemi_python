n = int(input())
i = 1
while True:
    if i ** 2 > n:
        print(i)
        break
    else:
        i += 1
        continue