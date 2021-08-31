##### Unix 'ls -lh' on Python

По аналогии с командой `ls -lh` для Unix систем, реализуйте модуль на Python который отображает содержимое директории 
<br><br>

Примечания:
 1. Что-бы получить содержимое директории используйте `os.listdir`
 1. Используйте `os.stat` что-бы получить инфромацию о каждом файле
 1. Используйте библиотеку [prettytable](http://zetcode.com/python/prettytable/) 
    <br>
   `pip install prettytable`
    <br>
    Имена столбцов: Mode, Owner, Group, Size, File name
 1. Используйте библиотеки `pwd` и `grp` что-бы получить имя пользователя и группу
 