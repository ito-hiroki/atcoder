D = int(input())
N = int(input())
ans = [0] * (D+1)
for _ in range(N):
    L, R = list(map(int, input().split()))
    ans[L-1] += 1
    ans[R] -= 1

tmp = 0
for i in ans[:-1]:
    tmp += i
    print(tmp)
