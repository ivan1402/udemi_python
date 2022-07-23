# 1 2 3 4 5 6 7 8 9
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lst_in = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_in = list(map(int, input().split()))
N = int(len(lst_in) ** 0.5)
print([[i for i in lst_in[N*j:(N*j + N)]] for j in range(N)])
