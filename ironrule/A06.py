N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

tmp = 0
cumsum_A = [0]
for a in A:
    tmp += a
    cumsum_A.append(tmp)

for _ in range(Q):
    L, R = list(map(int, input().split()))
    print(cumsum_A[R] - cumsum_A[L-1])
