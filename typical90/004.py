H, W = list(map(int, input().split()))
A = []
A_width = [0] * W
A_height = []

for i in range(H):
    tmp = list(map(int, input().split()))
    A.append(tmp)
    A_height.append(sum(tmp))
    for j, el in enumerate(tmp):
        A_width[j] += el

for h in range(H):
    tmp = [str(A_height[h] + A_width[w] - A[h][w]) for w in range(W)]
    print(" ".join(tmp))
