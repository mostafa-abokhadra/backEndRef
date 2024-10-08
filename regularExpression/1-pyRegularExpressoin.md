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
8. ? Zero or one occurrences e:g "he.?o"
```py
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x = re.findall("he.?o", txt)
print(x)
#This time we got no match, because there were not zero, not one,
# but two characters between "he" and the "o"
# output []
```
9. {} Exactly the specified number of occurrences e:g "he.{2}o"
```py
txt = "hello planet"
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x = re.findall("he.{2}o", txt)
print(x)
# output ['hello']
```
10. | Either or	e:g "falls|stays"
```py
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
# output
# ['falls']
# Yes, there is at least one match!
```
11. () Capture and group

### Special Sequence
- it is A \ followed by one of the characters in the list below, and has a special meaning:

1. \A Returns a match if the specified characters are at the beginning of the string
```py
txt = "The rain in Spain"
#Check if the string starts with "The":
x = re.findall("\AThe", txt) # it's function similar to ^
```

2. \b
- Returns a match where the specified characters are at the beginning or at the end of a word
- (the "r" in the beginning is making sure that the string is being treated as a "raw string")
```py
txt = "The rain in Spain"
#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt) # output []

#Check if "ain" is present at the end of a WORD:
re.findall(r"ain\b", txt) # ['ain', 'ain']
```
> [!NOTE]
> find more special sequence and sets here [w3s](https://www.w3schools.com/python/python_regex.asp)

### findall()
### search()
### split()

### Ref
- [w3s](https://www.w3schools.com/python/python_regex.asp)