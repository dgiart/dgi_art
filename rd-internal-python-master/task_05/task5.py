"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""




def mults(n1: int, n2: int, N: int):
    summa = 0
    for i in range(N):
        if i % n1 == 0 or i % n2 == 0:
            summa += i
    return summa


if __name__ == '__main__':
    print(mults(3, 5, 10))