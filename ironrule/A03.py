N = int(input())
ans = ""
for i in range(10):
    rem = N % 2
    ans = str(rem) + ans
    N = N // 2
print(ans)
