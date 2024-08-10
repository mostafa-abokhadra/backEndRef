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

# Asynchronous comprehensions are only allowed inside an async def function.
result = [await fun() for fun in funcs if await smth]
result = {await fun() for fun in funcs if await smth} # set comprehension
result = {fun: await fun() for fun in funcs if await smth} # dictionary comprehension
result = {fun: await fun() async for fun in funcs if await smth} # dictionary comprehension


dataset = {data for line in aiter()
                async for data in line
                if check(data)}
"""
    Basically you just need to add Python's new async keyword into your expression
    and call a callable that has implemented """__aiter__""". Trying to follow this
    syntax will actually result in a SyntaxError though:
"""
>>> result = [i async for i in range(100) if i % 2]
SyntaxError: invalid syntax

import asyncio
async def test(): 
    return [i async for i in range(100) if i % 2]
loop = asyncio.get_event_loop()
loop.run_until_complete(test())

"""
    If you run this code, you will get a TypeError: async for requires an object with __aiter__ method,
    got range. What you really want to do is call another async def function instead of calling range
    directly. Here s an example:
"""
# file
import asyncio
async def numbers(numbers):
    for i in range(numbers):
        yield i
        await asyncio.sleep(0.5)
async def main():
    odd_numbers = [i async for i in numbers(10) if i % 2]
    print(odd_numbers)
if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()
"""
    Technically the numbers function is an asynchronous generator
    that is yielding values to our asynchronous list comprehension.
"""

"""
    The return type of generator functions can be annotated
    by the generic type Generator[yield_type, send_type, return_type] 
"""
from typing import Generator
def generate() -> Generator[int, None, None]:
    for i in range(10):
        yield i
l = [i for i in generate()]

## better way
"""
    I'm using the typing specification below, using Iterator[int] instead of Generator.
    The validation is OK. I think it is a lot clearer. It better describes the code
    intention and is recommended by Python docs
    It would also allow future refactorings if you change your Generator for a list or other iterable.
"""
from typing import Iterator
# from collections.abc import Iterator python 3.10 and above

def generate() -> Iterator[int]:
    for i in range(10):
        yield i

# code task 1
"""
    Write a coroutine called async_generator that takes no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module.
"""
import random
from typing import Generator
import asyncio
async def async_generator() -> Generator[float, None, None]:
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

# code task 2
"""
    Import async_generator from the previous task and then write
    a coroutine called async_comprehension that takes no arguments.
    The coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
"""
import asyncio
from typing import List
async_generator = __import__('./0-async_generator').async_generator
async def async_comprehension() -> List[float]:
    return [_ async for _ in async_generator()]