https://peps.python.org/pep-0530/
https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/
https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3

# Learing objectives
"""
    How to write an asynchronous generator
    How to use async comprehensions
    How to type-annotate generators
"""

"""
    Python has extensive support for synchronous comprehensions,
    allowing to produce lists, dicts, and sets with a simple and concise syntax.
"""

# To illustrate the readability improvement, consider the following example
result = []
async for i in aiter():
    if i % 2:
        result.append(i)
# With the proposed asynchronous comprehensions syntax, the above code becomes as short as:
result = [i async for i in aiter() if i % 2]
# The PEP also makes it possible to use the await expressions in all kinds of comprehensions:
result = [await fun() for fun in funcs]