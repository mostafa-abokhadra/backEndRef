```py
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
```
### methods
1. findall() returns a list containing all matches
2. search() returns a match object if there is a match anywhere in the string
3. split() returns a list where the string has been split at each match
4. sub() replace one or many matches with a string

### metacharacter
- these are characters with a special meanings

1. [] a set of characters e:g `[a-m]`
```py
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)
# output ['h', 'e', 'a', 'i', 'i', 'a', 'i']
```
2. \ Signals a special sequence (can also be used to escape special characters) e:g `"\d"`
```py
txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)
print(x)
# output ['5', '9']
```