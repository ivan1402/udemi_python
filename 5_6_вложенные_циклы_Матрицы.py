"""
for i in range(1, 4):
    for j in range(1, 6):
        print(f'i = {i}, j === {j}', end= ' ')
    print()

# i = 1, j === 1 i = 1, j === 2 i = 1, j === 3 i = 1, j === 4 i = 1, j === 5
# i = 2, j === 1 i = 2, j === 2 i = 2, j === 3 i = 2, j === 4 i = 2, j === 5
# i = 3, j === 1 i = 3, j === 2 i = 3, j === 3 i = 3, j === 4 i = 3, j === 5
"""
"""
a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
b = [[3, 4, 5, 6], [1, 2, 3, 4], [2, 3, 4, 5]]
c = []
for i, row in enumerate(a): # i = 0 row = []
    r = []
    #print(r)
    for j, x in enumerate(row): # j = 0 x = 1
        r.append(x + b[i][j])   # x = 1 b = 3
        #print(r)
    c.append(r)

print(c) # [[4, 6, 8, 10], [3, 5, 7, 9], [5, 7, 9, 11]]
"""
