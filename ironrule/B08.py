table = [[0] * 1501 for _ in range(1501)]
N = int(input())
for _ in range(N):
    X, Y = list(map(int, input().split()))
    table[X][Y] += 1

for x in range(1, 1501):
    for y in range(1, 1501):
        table[x][y] = table[x][y] + table[x][y-1]

for y in range(1, 1501):
    for x in range(1, 1501):
        table[x][y] = table[x][y] + table[x-1][y]

Q = int(input())
for _ in range(Q):
    a, b, c, d = list(map(int, input().split()))
    print(table[c][d] + table[a-1][b-1] - table[a-1][d] - table[c][b-1])
