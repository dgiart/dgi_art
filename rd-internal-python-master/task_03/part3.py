import re
import collections

def letter_counter1(text: str):
    letters_dict = {}
    letters = re.findall('[a-zA-Z]', text.lower())
    for let in letters:
        if let in letters_dict:
            letters_dict[let] += 1
        else:
            letters_dict[let] = 1
    max_letter = 0
    for let in letters_dict:
        if letters_dict[let] > max_letter:
            max_letter = letters_dict[let]
            letter = let
    return max_letter, letter


def letter_counter2(text: str):
    letter_cnt = collections.Counter((re.sub(' +|[^a-zA-Z]', '',  text)).lower())
    return letter_cnt.most_common(1)


def python_counter(text: str):
    return len(re.findall('\spython\s', text.lower()))

if __name__ == '__main__':
    text = '''Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales. In July 2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years.
    Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.
    Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation. '''
    t = "abbccc"
    print(letter_counter2(text))
    print(python_counter(text))
