# Strings
# inside single qoutes or double qoutes
print("yes 'sir'"); print('yes "sir"')
print('''
mostafa
      abokhadra''') # using trible single qoute will print
                    # the string as your write exactly 
                    # including all new lines and spaces
print("""
mostafa
      abokhadra""") # using trible double qoute will print
                    # the string as your write exactly 
                    # including all new lines and spaces

# slicing
my_str = "mostafa abokhadra"
print(my_str[0], my_str[-1])
print(my_str[0:10]) # [start: end] , end not included
print(my_str[0: 10: 2]) # [start: end: steps]
print(my_str[:10])
print(my_str[3:])
print(my_str[:]) # the whole string
len(my_str)

# strip()
a_str = "     e        spaces       e  "
print (a_str.strip()) # it removes leading and trailing spaces
print(a_str.rstrip()) # right strip only, (remove the trailing spaces)
print(a_str.lstrip()) # left strip only (remove leading spaces)
print(a_str.strip("#@%$#")) # you can specify the characters to remove
                            # you can specify more than one character
# title() capatilize first char from each word and letters after numbers also is capatilized

num_str = "1"
# capitalize() capatilize first char from each word
# zfill() zero fill, it takes the width of the needed output
# for example num_str.zfill(3) will produce the output 001
# upper() convert all letters in the word to capital letters
# small() "" "" to small letters

a_str = "mostafa abokhadra"
print(a_str.split()) # ["mostafa", "abokhadra"]
# you can choose a separator
a_str = "mos-ta-fa-abokhadra"
print(a_str.split('-', 2)) # takes the delimeter and max time split
# max split is 2 times so the remaining string will be in the last string in the list 
# ["mos", "ta", "fa-abokhadra"]
# rsplit() # it splits but from right
# center(9) # takes the number of character you want to return 
name = "mostafa"
print(name.center(11)) #  mostafa  
print(name.center(11, '$')) # $$mostafa$$ 

a_str.count("someStr", 0, 10) # count how many time a substr is
# repeated in a certain string from position 0 to 10
name.swapcase() # convert small to capital and capital to small
name.startswith("mos") # takes the word, start postion and end position
name.startswith("mos", 3, 7) # false, as the search will be from the 3rd index
name.endswith("taf", 0, 6) # true

# to lesson 14 ^