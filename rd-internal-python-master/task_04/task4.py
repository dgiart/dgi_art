def min_value(values: list):
    min_value = 0
    for val in values:
        if val < min_value:
            min_value = val
    return min_value


def max_value(values: list):
    max_value = 0
    for val in values:
        if val > max_value:
            max_value = val
    return max_value


def list_to_ints(symbols: list):
    int_list = []
    for symbol in symbols:
        try:
            int_list.append(int(symbol))
        except ValueError as e:
            pass
        except TypeError as e:
            pass
    return f"Max = {max_value(int_list)}, Min = {min_value(int_list)}"


if __name__ == '__main__':
    numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
    print(list_to_ints(numbers))
