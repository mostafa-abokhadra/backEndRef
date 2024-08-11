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