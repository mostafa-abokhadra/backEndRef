### datetime
```python
import datetime
current = datetime.datetime.now() # current date and time
datetime.datetime.now().year
datetime.datetime.now().month 
datetime.datetime.now().day 
datetime.datetime.now().time() # return time part
datetime.datetime.now().time().hour # return time part
datetime.datetime.now().time().second # return time part
birth = datetime.datetime(2002, 12, 29)
print(f"i live for {(current - birth).days} days")
```