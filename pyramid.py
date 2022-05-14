def build(n):
    if n != 0:
        build(n - 1)
        print(n)
    else:
        print("base")


def oneToN(n, baseCase):
    if n!= baseCase:
        n += 1
        print(n-1)
        return oneToN(n, baseCase)
    else:
        print("end", n)


if __name__ == '__main__':
    oneToN(1, 3)
