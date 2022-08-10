a = set()
b = ''
while b != 'q':
    b = input()
    if b == 'q':
        break
    else:
        a.add(b)
print(len(a))
