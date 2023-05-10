H, W, N = list(map(int, input().split()))

table = [[0] * (W+1) for _ in range(H+1)]

for _ in range(N):
    A, B, C, D = list(map(int, input().split()))
    table[A-1][B-1] += 1
    table[A-1][D] -= 1
    table[C][B-1] -= 1
    table[C][D] += 1

for i in range(H):
    for j in range(1, W):
        table[i][j] += table[i][j-1]

for j in range(W):
    for i in range(1, H):
        table[i][j] += table[i-1][j]

for i in range(H):
    print(" ".join(map(str, table[i][:-1])))
