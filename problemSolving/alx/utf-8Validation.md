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

[!TIP]
Unicode is a character set. It translates characters to numbers.
UTf-8 is an encoding standard. It translates numbers into binary.

[!IMPORTANT]
- Computers store data, including text characters, as binary (1s and 0s).
- ASCII was an early way of encoding, or mapping characters to binary code so that computers could store them. However, ASCII did not provide enough room for non-Latin characters and numbers to be represented in binary
- Unicode was the solution to this problem. Unicode assigns a unique “code point” to every character in every human language.
- UTF-8 is a Unicode character encoding method. This means that UTF-8 takes the code point for a given Unicode character and translates it into a string of binary.
- It also does the reverse, reading in binary digits and converting them back to characters.
- UTF-8 is currently the most popular encoding method on the internet because it can efficiently store text containing any character.
- UTF-16 is another encoding method, but is less efficient for storing text files (except for those written in certain non-English languages).

