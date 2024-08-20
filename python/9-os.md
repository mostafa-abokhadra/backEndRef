```
import os
os.getcwd() # main current working directory
os.path.abspath(filename) # returns absolute path
# if you want to know the absolute path of the current opened file that you code in 
os.path.abspath(__file__)
os.path.dirname(filePath) # directory of the opened file
os.chdir() # change current directory
path = '\dir\dir2\dir3\n4' # note that this is a path, but when the comiler reach to \n4
# it will think it's a new line so use raw string
path = r"\n1\n4"
os.remove("filepath") # to delete a file
```