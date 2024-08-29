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
3. . Any character (except newline character) e:g `"he..o"`
```py
txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x)
# output ['hello']
```
4. ^ Starts with e:g `"^hello"`
```py
txt = "hello planet"
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
# output Yes, the string starts with 'hello'
```
5. $ Ends with e:g "planet$"
```py
txt = "hello planet"
#Check if the string ends with 'planet':
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
#ouput Yes, the string ends with 'planet'
```
6. * Zero or more occurrences e:g "he.*o"
```py
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
print(x)
# output ['hello']
```
7. + One or more occurrences e:g "he.+o"
```py
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
print(x)
# output ['hello']
```
