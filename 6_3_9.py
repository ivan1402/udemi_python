t = ((1, 0, 0, 0, 0), # 0.0 N = 5
     (0, 1, 0, 0, 0), # 1.1
     (0, 0, 1, 0, 0), # 2.2
     (0, 0, 0, 1, 0), # 3.3
     (0, 0, 0, 0, 1)) # 4.4
#N = int(input())
N = 3
t2 = tuple([tuple([y for y in i[:N]]) for i in (t[x] for x in range(N))])
for i in range(N):
    print(*t2[i])
