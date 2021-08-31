prefixes = ['B', 'Kb', 'Mb', 'Gb', 'Tb']


def file_size(size: int):
    power = 0

    while True:
        try:
            # if power > 5:
            #     break
            if 2 ** (10 * power) <= size < 2 ** (10 * (power + 1)):
                num_res = round(size / (2 ** (10 * power)), 1)
                res = f"{num_res}{prefixes[power]}"
                return res
            power += 1

        except IndexError as e:
            print(1111)
            return 'File Size is out of range'


if __name__ == '__main__':
    print(file_size(12389485008592525235))