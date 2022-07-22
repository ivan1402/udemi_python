#list_int = [4, 5, 2, 0, 6, 3, -56, 3, -1]
list_int = list(map(int, input().split()))
k = 0
for j, x in enumerate(list_int):
    i = k
    k += 1
    while i != len(list_int):
        if x >= list_int[i]:
            x = list_int[i]
            list_int[j], list_int[i] = list_int[i], list_int[j]
        i += 1
print(*list_int)

