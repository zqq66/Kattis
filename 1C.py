

def PieceofCake(n, h, v):
    if h < n / 2:
        h = n - h
    if v < n / 2:
        v = n - v

    print(4 * h * v)


if __name__ == '__main__':
    n, h, v = [int(i) for i in input().split()]
    PieceofCake(n, h, v)