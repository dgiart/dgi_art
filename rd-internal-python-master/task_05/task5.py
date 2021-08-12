
def mults(n1: int, n2: int, N: int):
    summa = 0
    for i in range(N):
        if i % n1 == 0 or i % n2 == 0:
            summa += i
    return summa


if __name__ == '__main__':
    print(mults(3, 5, 1000))