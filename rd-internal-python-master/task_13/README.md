
##### Context manager

Реализуйте контекстный менеджер `timer`


Примечания:
 * используйте `__enter__` и `__exit__`



##### <u>Check yourself</u>:
```
with timer('doing some sleeps'):
    time.sleep(1)
    time.sleep(2)
    time.sleep(3)
    
Output:
timer: block 'doing some sleeps' executed in 6.013 sec
```