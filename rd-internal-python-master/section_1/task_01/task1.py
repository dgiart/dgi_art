import sys
import re


def check_password(p: str):
    '''
    returns if p is a good password
    :param p:
    :return:
    '''
    if not isinstance(p, str):
        print(f"error: {p} is not a string")
        return False
    if len(p) <= 8:
        print("error: too short, min length is 8")
        return False
    if not re.search(r'\d', p):
        print("error: should contain at least one digit")
        return False
    if not re.search('[a-z]', p):
        print("error: should contain at least one lowercase letter")
        return False
    if not re.search('[A-Z]', p):
        print("error: should contain at least one uppercase letter")
        return False
    print("Looks good!")
    return True


if __name__ == '__main__':
    p = "aaaBBBBBBBBBBBBBBBBBBBBB7BB"
    # print(re.match('[a-z]', p))
    # p = 'ABAD#&&1zz'
    check_password(p)
