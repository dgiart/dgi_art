summa = 0


def sum_of_elements(elements: list):
    global summa
    for el in elements:
        if isinstance(el, list):
            sum_of_elements(el)
        else:
            summa += el
    return summa


if __name__ == '__main__':
    l = [1, [], 2, [-19, 700, 0, [90, 33, [18, 77, [0, ], -2], 11, 16], -100]]
    l2 = [1,  2, -19, 700, 0, 90, 33, 18, 77, -2, 11, 16, -100]
    print(sum_of_elements(l))