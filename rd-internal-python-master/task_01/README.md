/home/art/programming/python
##### Password Validation

Реализуйте функцию для проверки стойкости паролей.

Пароль считается "стойким" если удовлетворяет следующим условиям: 
 * длинна не меннее 8 символов
 * содержит ловеркейс и апперкейс буквы
 * содержит хотя бы одну цифру

Пример: 
```
def check_password(p):
    # print errors if any
    return True/False
```
<br>

##### <u>Check yourself</u>: 
```
>>> check_password('hello')
error: too short, min length is 8
error: should contain at least one digit
error: should contain at least one uppercase letter

>>> check_password('TERMINATOR3000')
error: should contain at least one lowercase letter

>>> check_password(700)
error: 700 is not a string

>>> check_password('HelloWorld2018')
Looks good!
```