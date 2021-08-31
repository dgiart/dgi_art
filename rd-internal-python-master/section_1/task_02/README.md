
##### List filtering

Дан объект типа list():<br>
 `l = [1, 2, '3', 4, 'name', 10, 33, 'Python']` 

Релизуйте функцию которая отфильтровует только `integer` значения из этого листа.

Напишите несколько вариантов решения:
 * используя цикл for
 * используя list comprehensions
 * используя filter() + lambda

Пример: 

```
def filter_list(l):
    return  # [1, 2, 4, 10, 33]
```
<br>

##### <u>Check yourself</u>: 
```
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
```