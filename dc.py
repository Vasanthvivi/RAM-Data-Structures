def findSqrt(n):
    if n == 0 or n == 1:
        return n

    i = 1
    r = 1
    steps = 1
    while (r <= n):
        i += 1
        steps += 1
        r = i * i
    print(f"number of steps taken {steps}")
    print(i - 1)


def sqrt(n):
    s = 1
    value = n
    end = int(n / 2)
    ans = 0
    steps = 1
    while s <= end:
        steps = steps + 1
        m = int((s + end) / 2)
        if m * m == value:
            print(f"number of steps taken {steps}")
            return m
        if m * m < value:
            s = m + 1
            ans = s
        if m * m > value:
            end = m - 1
            ans = m - 1
    print(f"number of steps taken {steps}")
    return ans


if __name__ == "__main__":
    print("in DC method")
    sqrt(15625)
    print("in brute force method")
    findSqrt(15625)

