##### IP validation

Напишите функцию для валидации IP-адреса. 


Пример:
```
def check_ip(ip_address):
    return True/False
```
<br>

Напишите несколько вариантов решения:
 * используя библиотеку `re`
 * используя `socket.inet_aton`
 
 
###### Check yourself
```
assert check_ip('') is False
assert check_ip('192.168.0.1') is True
assert check_ip('0.0.0.1') is True
assert check_ip('10.100.500.32') is False
assert check_ip(700) is False
assert check_ip('127.0.1') is True
```
 
 
