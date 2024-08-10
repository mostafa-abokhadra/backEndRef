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
"""
    In Python, aiter() is a built-in function that returns an asynchronous iterator 
    from an asynchronous iterable. It is used when working with asynchronous code,
    particularly with async for loops.
    Asynchronous Iteration: Just like iter() is used to get an iterator from a regular iterable
    (e.g., lists, tuples), aiter() is used to get an asynchronous iterator from an asynchronous iterable.
    Async Iterables: These are objects that implement the __aiter__() method and optionally the __anext__() method.
    Usage Context: Typically used in asynchronous programming with async for loops,
    allowing you to iterate over asynchronous data sources.
"""
class AsyncIterable:
    def __init__(self):
        self.count = 0
    def __aiter__(self):
        return self
    async def __anext__(self):
        if self.count < 5:
            self.count += 1
            return self.count
        else:
            raise StopAsyncIteration
"""
    What Happens Here:
    AsyncIterable Class: This class defines an asynchronous iterable that counts from 1 to 5.
    __aiter__ Method: Returns the asynchronous iterator itself (self).
    __anext__ Method: Defines the next item to be returned in the iteration.
        It will increment the counter until it reaches 5, then it raises StopAsyncIteration to end the loop.
    aiter(AsyncIterable()): This converts the AsyncIterable instance into an asynchronous iterator.
    async for Loop: Iterates over the asynchronous iterator, printing the numbers from 1 to 5.
    In summary, aiter() is essential when you need to obtain an asynchronous iterator from an asynchronous iterable
    in Python, enabling asynchronous iteration with async for.
"""

async def main():
    async for number in aiter(AsyncIterable()):
        print(number)

import asyncio
asyncio.run(main())


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

# code task 3
"""
    Import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
    Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension
async def measure_runtime():
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension()
        async_comprehension(), async_comprehension())
    end = time.time()
    return time.perf_counter() - start_time