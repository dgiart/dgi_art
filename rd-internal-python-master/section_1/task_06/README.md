
##### Broken Application

В приложении `broken_app` есть циклические импорты. Его нельзя запустить из командной строки
```
$ python app.py
Traceback (most recent call last):
  ...
ImportError: cannot import name setup_database
```
<br>

Решите проблему несколькими способами:
 1. Перенесите строку `from database_client import setup_database` внутрь фунции `main()`
 1. Измените `from database_client import setup_database` на `import database_client` 
 1. Перепишите приложение. Добавьте новый модуль `settings.py`
 
 
