#!/usr/bin/env python3
import re

about = "mostafa abokhadra is the a python backend developer"

print(re.search('abokhadra', about).group()) # abokhadra
print(re.search('abokhadra', about).span()) # (8, 17)
print(re.search('abokhadra', about).string) # mostafa abokhadra is the a python backend developer


# [] a set of characters that you wish to match.
# first occurance will be matched if used with re.search()
# Characters can be listed individually, or a range of characters
# any metacharacter inside [] is stripped of its special nature, so you can match them

print(re.search('[a-z]', about).group()) # m
print(re.search('[a-z]', about).span()) # (0, 1)
print(re.search('[python]', about).group()) # o
print(re.search('[python]', about).span()) # (1, 2)


someString = '55534 mostafa $ 4445 abokhadra ^^'
# will match 5 and ^ characters (first occurance)
print(re.search('[5^]', someString).group()) # 5
# will match anything except 5
print(re.search('[^5]', someString).group()) # 3

# \ metacharacter
""" if you need to match a [ or \
    you can precede them with a backslash to
    remove their special meaning: \[ or \\.
"""
""" 
\d
    Matches any decimal digit; this is equivalent to the class [0-9].
\D
    Matches any non-digit character; this is equivalent to the class [^0-9].
\s
    Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
\S
    Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
\w
    Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
\W
    Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].

These sequences can be included inside a character class. For example, [\s,.] 
    is a character class that will match any whitespace character, or ',' or '.'
"""

# . metacharacter
"""
    It matches anything except a newline character
"""

# *
"""
    it doesn't match the literal character '*' instead, it specifies that the previous
    character can be matched zero or more times, instead of exactly once.
    
    for example, ca*t will match 'ct' (0 'a' characters),
    'cat' (1 'a'), 'caaat' (3 'a' characters), and so forth.
"""

# read engin file in this directory

"""
    There are two more repeating operators or quantifiers. The question mark character ?
    matches either once or zero times, you can think of it as marking something as being
    optional. For example, home-?brew matches either 'homebrew' or 'home-brew'.
    
    The most complicated quantifier is {m,n}, where m and n are decimal integers.
    This quantifier means there must be at least m repetitions, and at most n.
    For example, a/{1,3}b will match 'a/b', 'a//b', and 'a///b'. It won't match 'ab', which
    has no slashes, or 'a////b', which has four.
    
    You can omit either m or n; in that case, a reasonable value is assumed for the missing
    value. Omitting m is interpreted as a lower limit of 0, while omitting n results in an upper
    bound of infinity.
    
    The simplest case {m} matches the preceding item exactly m times. For example,
    a/{2}b will only match 'a//b'.
    
    Readers of a reductionist bent may notice that the three other quantifiers can all be
    expressed using this notation. {0,} is the same as *, {1,} is equivalent to +,
    and {0,1} is the same as ?. It's better to use *, +, or ? when you can,
    simply because they're shorter and easier to read.
"""
# backslash plague
"""
https://docs.python.org/3/howto/regex.html#the-backslash-plague
"""

# continue from https://docs.python.org/3/howto/regex.html#performing-matches

# ref
"""
https://docs.python.org/3/howto/regex.html
"""



