https://realpython.com/async-io-python/
https://docs.python.org/3/library/asyncio.html
https://docs.python.org/3/library/random.html #random.uniform

## learning objectives
"""
    async and await syntax
    How to execute an async program with asyncio
    How to run concurrent coroutines
    How to create asyncio tasks
    How to use the random module
"""
import time
start_time = time.time()
time.sleep(4)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
# here the code will implement sequentially as we used time module not asyncio module

"""
    async IO is a single-threaded, single-process design:
    it uses cooperative multitasking, It has been said in
    other words that async IO gives a feeling of concurrency
    despite using a single thread in a single process.
    Coroutines (a central feature of async IO) can be scheduled concurrently,
    but they are not inherently concurrent.
"""

# How does something that facilitates concurrent code use a single thread and a single CPU core?
"""
    Chess master Judit hosts a chess exhibition in which she plays multiple amateur players.
    She has two ways of conducting the exhibition: synchronously and asynchronously.
    > Assumptions:
    > - 24 opponents
    > - Judit makes each chess move in 5 seconds
    > - Opponents each take 55 seconds to make a move
    > - Games average 30 pair-moves (60 moves total)
    > 
    > Synchronous version: Judit plays one game at a time, never two at the same time,
    until the game is complete. Each game takes (55 + 5) * 30 == 1800 seconds, or 30 minutes.
    The entire exhibition takes 24 * 30 == 720 minutes, or 12 hours.
    > 
    > Asynchronous version: Judit moves from table to table,
    making one move at each table. She leaves the table and
    lets the opponent make their next move during the wait time.
    One move on all 24 games takes Judit 24 * 5 == 120 seconds,
    or 2 minutes. The entire exhibition is now cut down to 120 * 30 == 3600 seconds,
    or just 1 hour.

    There is only one Judit , who has only two hands and makes only one move at a time by herself.
    But playing asynchronously cuts the exhibition time down from 12 hours to one. So,
    cooperative multitasking is a fancy way of saying that a program's event loop 
    communicates with multiple tasks to let each take turns running at the optimal time.
"""

### asyncio
https://www.youtube.com/watch?v=K56nNuBEd0c
def brewCoffe():
	print("start coffe")
	time.sleep(3)
	print("end coffe")
def toastingBread();
	print("start tosting")
	time.sleep(2)
	print("end toasting")
brewCoffe()
toastingBread()

"""
    this code is sequential, brewCoffe function should finish before toastingBread starts,
    but you can brew your coffe and toasting your bread concurrently right :)
    so to save us some time we will turn this code to execute concurrently
    to turn each function into coroutine (a function that run conccurently with other code)
    you add the key word "async" in the prototype
    but this is not suffecient you also have to specify weher in the coroutine it is safe to pause and
    yeild control to other coroutines using "await" key word
    you can only put await in front of commands that is awaitable, the time.sleep function is not awaitable
    but asyncio.sleep is awaitable
    async module has a method called "gather" to group coroutines for concurrent execution,
    the arguments determine which coroutines will run concurrently, calling a coroutine returns
    a coroutine object not a typical return value even though the argument appear as a regular function calls,
    this coroutine object give the asyncio the ability to start and stop their execution, and to get the return
    value from the coroutines you need to await them.
    any function that has the await key word must be declared as async function
    instead of using gather function you can call each coroutine separately using create_task method
"""
async def brewCoffe():
	print("start coffe")
	await asyncio.sleep(3)
	print("end coffe")
async def toastingBread();
	print("start tosting")
	await asyncio.sleep(2)
	print("end toasting")
async def main():
	batch = asyncio.gather(brewCoffe(), toastingBread())
	brewCoffeResult, toastringBreadResult = await batch
	# order of return values matter
	# use of await here is not optional 
	# becaue main has now become a coroutine we have to call in a slightly
	# different way
if __name__ == '__main__':
	asyncio.run(main())
	
# also you can call each coroutine separately using create_task method
async def main():
	coffe_task = asyncio.create_task(brewCoffe())
	toasting_task = asyncio.creat_task(toastingBread())
	brewCoffeResult = await coffe_task
	toastringBreadResult = await toasting_task

##########################################################################################################

# file
import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    seconds: float = random.uniform(0, max_delay)
    await asyncio.sleep(seconds)
    return seconds

# file
import asyncio
    from typing import List
    wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    listy = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        sec = await task
        listy.append(sec)
    return sorted(listy)

# better way
async def wait_n(n: int, max_delay: int) -> List[float]:
    resolves = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(resolves)


"""
    The `*` symbol before the function call in the context of asyncio.gather is known as the
    "unpacking" or "splat" operator. It is used to unpack a collection of items
    (like a list, tuple, or generator) into individual arguments for a function call.

    Here is what happens step-by-step:
    1. Generator Expression:
    (wait_random(max_delay) for i in range(n))
    This part creates a generator that will produce `n` coroutines of wait_random(max_delay)

    2. Unpacking with * Operator:
    *(wait_random(max_delay) for i in range(n))
    The `*` operator unpacks the generator, effectively turning the generator into individual arguments
    for the asyncio.gather function. 
    For example, if n is 3, the generator expression would create three 
    wait_random(max_delay) coroutines. The `*` operator would then unpack these into:
    asyncio.gather(wait_random(max_delay), wait_random(max_delay), wait_random(max_delay))
    Finally, asyncio.gather takes these unpacked coroutines and runs them concurrently.
   """

### Without Unpacking:
"""
    If you didn't use the `*` operator, you'd pass the generator object
    itself as a single argument to asyncio.gather, which wouldn't work as
    intended because asyncio.gather expects multiple coroutine objects,
    not a single generator object.
"""
### Example:
# Consider a simpler example to illustrate the `*` operator:

def print_args(a, b, c):
    print(a, b, c)
args = (1, 2, 3)
print_args(*args)  # This is equivalent to print_args(1, 2, 3)

""" In this example, the tuple args is unpacked into individual arguments `1`, `2`, and `3`,
    which are then passed to `print_args`.

    conclusion:- 
    - The `*` operator unpacks a collection (like a list, tuple, or generator)
    into individual arguments for a function call.
    - In the context of `asyncio.gather`, it is used to unpack the generator of coroutines into individual
    coroutine arguments that `asyncio.gather` can then run concurrently.
"""

# file
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()
    return (end - start)

# file
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random
async def task_wait_n(n: int, max_delay: int) -> List[float]:
    listy = []
    for i in range(n):
        task = task_wait_random(max_delay)
        sec = await task
    listy.append(sec)
    return sorted(listy)

##### or
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random
async def task_wait_n(n: int, max_delay: int) -> List[float]:
    resolves = await asyncio.gather(
        *(task_wait_random(max_delay) for i in range(n)))
    return sorted(resolves)