N = int(input())

a = [[j for i in range(N)] for j in range(N)]

for i in a:
    print(*i)