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
### formating the date
```python
date = datetime.datetime(2002, 12, 29)
# string formating time (strftime) returns the time in string
data.strftime("%d - %B - %Y")
# search for strftime directives to see all of the ways
# that you can format the date with
```