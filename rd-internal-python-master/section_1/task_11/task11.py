# summa = 0

class Sum_of_elements:
    summa = 0
    def sum_of_elements(self, elements: list):
        for el in elements:
            if isinstance(el, list):
                self.sum_of_elements(el)
            else:
                self.summa += el
        return self.summa


if __name__ == '__main__':
    l = [1, [], 2, [-19, 700, 0, [90, 33, [18, 77, [0, ], -2], 11, 16], -100]]
    l2 = [1, 2, -19, 700, 0, 90, 33, 18, 77, -2, 11, 16, -100]
    l3 = [1, [5, 6, [13, 5]], 2, 3, [2, [-5, 6, [-7, [], 8]]], -50]
    l4 = [1, [5, 6, [13, 5]], 2, 3, [2, [-5, 6, [-7, [], 8]]], -50]
    l5 = [1, [5, 6, [13, 5]], 2, 3, [2, [-5, 6, [-7, [], 8]]], -50]
    s1 = Sum_of_elements()
    s2 = Sum_of_elements()
    s3 = Sum_of_elements()

    print(l3)
    print(s1.sum_of_elements(l3))
    print(l4)
    print(s2.sum_of_elements(l4))

    print(l5)
    print(s3.sum_of_elements(l5))
