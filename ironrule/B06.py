N = int(input())
A = list(map(int, input().split()))
tmp = 0
cumsum_A = [0]
for a in A:
    tmp += a
    cumsum_A.append(tmp)

Q = int(input())
for _ in range(Q):
    L, R = list(map(int, input().split()))
    if (cumsum_A[R] - cumsum_A[L-1] > (R-L+1)/2):
        print("win")
    elif (cumsum_A[R] - cumsum_A[L-1] < (R-L+1)/2):
        print("lose")
    else:
        print("draw")
