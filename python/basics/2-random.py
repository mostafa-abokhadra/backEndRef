import random
list1 = [1, 2, 3, 4, 5, 6]
# choise # Returns a random item from a list, tuple, or string
print(random.choice(list1))
#to obtain random samples from various data types.
random.sample(sequence, length)
#  Shuffling means changing the position of the elements of the sequence.
random.shuffle(list1)

#Returns a random integer within the range
# Return a random integer N such that 
# a <= N <= b. Alias for `randrange(a, b+1)`.
randint(1, 10) 
# Returns a random int number within the range
randrange()

# Generate random floating numbers between 0.0 to 1.
print(random.random())
# output: 0.8443722499369146

# The random.uniform(a, b) function in Python is used to generate a
# random floating-point number between two given numbers a and b.
# The number generated can include a, b, or any value in between.
random.uniform(a, b)