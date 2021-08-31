def filter_list1(l: list):
    int_l = []
    for el in l:
        if isinstance(el, int):
            int_l.append(el)
    return int_l


def filter_list2(l: list):
    int_l = [el for el in l if isinstance(el, int)]
    return int_l

def filter_list3(l: list):
    return list(filter(lambda x: isinstance(x, int), l))



if __name__ == '__main__':
    l = [1.3, 1, 'a', 2, 3, 's', '123']
    print(filter_list3(l))