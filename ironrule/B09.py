table = [[0] * 1501 for _ in range(1501)]

N = int(input())
for _ in range(N):
    A, B, C, D = list(map(int, input().split()))
    table[A][B] += 1
    table[A][D] -= 1
    table[C][B] -= 1
    table[C][D] += 1

for i in range(1501):
    for j in range(1, 1501):
        table[i][j] += table[i][j-1]

for j in range(1501):
    for i in range(1, 1501):
        table[i][j] += table[i-1][j]

ans = 0
for i in range(1501):
    for j in range(1501):
        if table[i][j] > 0:
            ans += 1

print(ans)
