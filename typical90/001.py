N, L = map(int, input().split(" "))
K = int(input())
A = list(map(int, input().split(" ")))


def calc_div_num(limit):
    pre = 0
    count = 0
    for el in A:
        if el - pre >= limit and L - el >= limit:
            count += 1
            pre = el
    return count >= K


left = -1
right = L + 1
while (right - left) > 1:
    mid = left + (right - left) // 2
    if calc_div_num(mid):
        left = mid
    else:
        right = mid

print(left)
