# utf-8 (Unicode Transformation Format)
### unicode
- Unicode is a universal character set that defines all the characters needed for writing the majority of living languages in use on computers.
- The Unicode Standard covers (almost) all characters, punctuations, and symbols in the world and enables processing, storage, and transport of text independent of platform and language.
### difference between unicode and utf-8
##### unicode
- unicode is a character set
- it is a list where all characters have a unique decimal number
- e:g A = 65, D = 69
- e:g decimal number that represent the string "hello" -> 104 101 108 108 111
##### utf-8
- it is encoding
- it is how unicode numbers are translated into binary numbers to be stored in computer
- UTF-8 encoding will store "hello" like this (binary): 01101000 01100101 01101100 01101100  01101111

![TIP]
Unicode is a character set. It translates characters to numbers.
UTf-8 is an encoding standard. It translates numbers into binary.