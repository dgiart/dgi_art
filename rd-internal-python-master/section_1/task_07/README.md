
##### File size conversion

Релизуйте функцию которая принимает размер файла в байтах (Byte) и преобразовует его в удобный для чтения формат: `Byte`, `Kilobyte`, `Megabyte`, `Gigabyte`
<br>
<br>
Сколько гигабайт (Gigabyte) в `sys.maxint` ?

Пример:
```
def file_size(size_in_bytes):
    # implement me
    return '12.6Mb'
```

 


Примечание:
 * String Format [examples](https://docs.python.org/2/library/string.html#format-examples)
 

###### Check yourself
```
assert file_size(19) == '19.0B'
assert file_size(12345) == '12.1Kb'
assert file_size(1101947) == '1.1Mb'
assert file_size(572090) == '558.7Kb'
assert file_size(999999999999) == '931.3Gb'
```





 