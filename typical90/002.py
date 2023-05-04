N = int(input())


def is_valid(text):
    count = 0
    for t in text:
        if t == "0":
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    if count == 0:
        return True
    return False


for i in range(2**N):
    text = format(i, f"0{N}b")
    if is_valid(text):
        print(text.replace("0", "(").replace("1", ")"))
