import re


def check_ip(ip_to_check: str):
    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    if re.match(pattern, ip_to_check):
        return True
    else:
        return False


if __name__ == '__main__':
    res = re.match(r"^\d{1,3}$", '123654789')
    print(res)