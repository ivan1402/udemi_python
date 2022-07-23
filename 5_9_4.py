lst_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 4, 3]]
A = [[i[row] for i in lst_in] for row in range(len(lst_in[0]))]
for row in A:
    print(*row)