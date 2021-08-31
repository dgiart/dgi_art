# Task

**REQUIREMENTS:**

Написать ф-ю is_number, которая будет принимать на вход строку и проверять является ли строка числом или нет
и возвращать bool

**REQUIREMENTS:**

Вывести из list_1 список квадратов всех позитивных значений типа int которые делятся на 2 без остатка используя
List Comprehensions

вывод: list

**REQUIREMENTS:**

Вывести из list_1 список кубов всех негативных значений типа float которые НЕ делятся на 2 без остатка, количество
знаков после запятой: 2 используя List Comprehensions

вывод: list

**REQUIREMENTS:**

Собрать предложение из слов из list_1 используя ф-ю is_number используя List Comprehensions

вывод: str


**REQUIREMENTS:**

Посчитать сумму всех негативных значений из list_1 используя ф-ю is_number используя List Comprehensions

вывод: float


**REQUIREMENTS:**

Используя dict comprehensions получить словарь из dict_1 в котором ключом будет имя, а значением будет
строка содрежащая через запятую два последних скила в случае если персонаж является джедаем, в обратном случае значением
должна быть роль.

**REQUIREMENTS:**

Написать генератор, который будет принимать на вход переменную sort_by_height_desc и итерировать её содержимое,
генератор должен быть написан в двух видах:
    - в виде функции
    - используя generator expression
присвоить генераторы переменным gen_1, gen_2

**REQUIREMENTS:**

Используя for loop, вывести содержимое обоих генераторов в консоль.

**TEST DATA:**
~~~~
list_1 = [
    "Comprehensions", 1, -1, "some", 7, 58.8, "34.46", "times ", -2, 3.6, -78.92, "123.1", "are", -8, "better", 3,
    "-46.78", 345, "than", -13.3, "'for'", 1.2, 9, 23.8, "loops.", 4, 5
]

dict_1 = {
    "Chewie": {
        "sex": "male",
        "age": 300,
        "height": 2.2,
        "role": "pilot",
        "skills": [
            "strenght", "extra hair", "reticence"
        ]
    },
    "Anakin Skywalker": {
        "sex": "male",
        "age": 22,
        "height": 1.8,
        "role": "jedi",
        "skills": [
            "speed", "high level of midichlorians", "honesty"
        ]
    },
    "Padme Amidala": {
        "sex": "female",
        "age": 19,
        "height": 1.6,
        "role": "queen",
        "skills": [
            "honesty", "trick", "bravery"
        ]
    },
    "R2D2": {
        "sex": "unknown",
        "age": 567,
        "height": 1.1,
        "role": "robot",
        "skills": [
             "bravery", "technical skills", "size"
        ]
    },
    "Yoda": {
        "sex": "male",
        "age": 450,
        "height": 0.9,
        "role": "jedi",
        "skills": [
             "high level of midichlorians", "wisdom", "experience"
        ]
    },
    "Sabe": {
        "sex": "female",
        "age": 15,
        "height": 1.7,
        "role": "servant",
        "skills": [
            "reticence", "sensitivity", "honesty"
        ]
    },
}
~~~~
