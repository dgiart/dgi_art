
##### Working with 'csv' and 'json' structures

Имеется файл `cars.csv`
<br>

Используйте библиотеку `csv` что бы прочитать содержимое файла.
Конвертируйте данные в формат `json` и сохраните в файл `cars.json`
<br>

Примечания:
 * используйте [csv.DictReader](https://docs.python.org/2/library/csv.html#csv.DictReader)
 * используйте [json.dump](https://docs.python.org/2/library/json.html#json.dump) с параметром `indent=2`
 * используйте контекстный менеджер `with` для создания файла
 

##### <u>Check yourself</u>:
```
bash$ cat ../task_12/cars.json
[
  {
    "Year": "1997",
    "Make": "Ford",
    "Model": "E350"
  },
  {
    "Year": "2000",
    "Make": "Mercury",
    "Model": "Cougar"
  },
  {
    "Year": "2006",
    "Make": "Dacia",
    "Model": "Logan"
  }
]
```

