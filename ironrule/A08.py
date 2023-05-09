H, W = list(map(int, input().split()))
X = []
X_cumsum = [[0] * (W + 1)]
for _ in range(H):
    x_in = list(map(int, input().split()))
    X.append(x_in)

    x_in_cumsum = [0]
    for i in x_in:
        x_in_cumsum.append(i + x_in_cumsum[-1])
    for i in range(W+1):
        x_in_cumsum[i] += X_cumsum[-1][i]

    X_cumsum.append(x_in_cumsum)

Q = int(input())
for _ in range(Q):
    A, B, C, D = list(map(int, input().split()))
    ans = X_cumsum[C][D] + X_cumsum[A-1][B-1] - X_cumsum[C][B-1] - X_cumsum[A-1][D]
    print(ans)
