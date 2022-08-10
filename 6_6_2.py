a = input().split()
d = {int(a[0]) + key: value for key, value in enumerate(a[1::])}
print(d.get(4))
