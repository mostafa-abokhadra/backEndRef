https://docs.python.org/3/library/typing.html
https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html # mypy cheatsheet

## learning objectives
"""
    Type annotations in Python 3
    How you can use type annotations to specify function signatures and variable types
    Duck typing
    How to validate your code with mypy
"""
# Python is a dynamically-typed language. That means that variable
# types are dynamically set at run-time, upon assignment of a value to a variable.
age: int = 1
num: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"
x: list[int] = [1]
x: set[int] = {6, 7}
x: dict[str, float] = {"field": 2.0}
x: tuple[int, str, float] = (3, "yes", 7.5)

# For tuples of variable size, we use one type and ellipsis
x: tuple[int, ...] = (1, 2, 3)
x: list[int | str] = [3, 5, "test", "fun"]

def show(value: str, excitement: int = 10) -> None:
    print(value + "!" * excitement)
# Note that arguments without a type are dynamically typed (treated as Any)

"""
    A type alias is defined using the [`type`] statement,
    which creates an instance of [`TypeAliasType`]
    In this example, Vector and list[float] will be treated
    equivalently by static type checkers:
"""
type Vector = list[float]
type ConnectionOptions = dict[str, str]
type Address = tuple[str, int]

### newType
from typing import NewType, List, Set, Dict, Tuple, Union, Optional,  Callable
from typing import NewType, Iterator

x: List[int] = [1]
x: Set[int] = {6, 7}
x: Dict[str, float] = {"field": 2.0}
x: Tuple[int, str, float] = (3, "yes", 7.5)
x: Tuple[int, ...] = (1, 2, 3)

UserId = NewType('UserId', int)
some_id = UserId(524313)
def get_user_name(user_id: UserId) -> str:
    ...
user_a = get_user_name(UserId(42351)) # passes type checking
user_b = get_user_name(-1) # fails type checking; an int is not a UserId

def add(a: float, b: float) -> float:{}
def concat(str1: str, str2: str) -> str:{}

from typing import List, Union, Tuple, Callable, Iterable, Sequence, Any, Mapping, TypeVar
def sum_list(input_list: List[float]) -> float:
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
"""mixedList is of type list that can hold integer or flaot values only"""
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
"""
v: is either an integer or a float, the function returns a tuple
constist of 2 items the first is string and the other is float
"""
def make_multiplier(multiplier: float) -> Callable[[float], float]:
"""the function return a callable (a function), this function take
one argumentas a float and returns a float value"""
    return lambda x: x * multiplier
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
T = TypeVar('T')
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:

"""
    Duck typing is a concept in programming that allows for more flexible
    and adaptable code. It is primarily associated with dynamic languages
    like Python. The term "duck typing" comes from the phrase
    "If it looks like a duck and quacks like a duck, it's probably a duck."
    In the context of programming, this means that the suitability of an object is
    determined by the presence of certain methods and properties, rather than the actual type of the object.
    In Python, duck typing allows you to use any object that provides the required behavior,
    regardless of its actual type. Here's a detailed explanation with examples:
"""
### 1. The Concept of Duck Typing
"""
    Duck typing focuses on what an object can do rather than what it is. 
    This allows for writing more flexible and reusable code.
    The object's compatibility is determined by the methods it implements,
    not by its inheritance from a particular class
"""
### 2. Example of Duck Typing
Let's consider an example where we have a function that expects an object to be able to "quack":

class Duck:
    def quack(self):
        print("Quack!")
class Person:
    def quack(self):
        print("I'm quacking like a duck!")
def make_it_quack(thing):
    thing.quack()
duck = Duck()
person = Person()
make_it_quack(duck)    # Quack!
make_it_quack(person)  # I'm quacking like a duck!

"""
    In this example, both `Duck` and `Person` classes have a `quack` method.
    The `make_it_quack` function accepts any object that has a `quack` method,
    regardless of its class. This is duck typing in action.
"""

### 3. Benefits of Duck Typing
"""
    Flexibility: You can pass different types of objects to the
    same function as long as they implement the required methods.
    Code Reusability: Functions and methods can operate on a wider
    variety of objects, making the code more reusable.
    -Polymorphism: Duck typing is a form of polymorphism
    where the object's behavior determines its suitability.
"""

### 4. Potential Drawbacks
"""
    - Less Explicit: Since type checking is not enforced, errors
    related to incompatible types might only appear at runtime.
    - Harder to Debug: It might be more challenging to debug issues
    since type-related errors are not caught at compile time.
"""

### 5. Example with Collections
Consider a function that processes collections:
def process_collection(collection):
    for item in collection:
        print(item)
# This works with any iterable, not just lists
process_collection([1, 2, 3])
process_collection((1, 2, 3))
process_collection({"a": 1, "b": 2, "c": 3}.items())

"""
    Here, the `process_collection` function works with any iterable collection,
    not just lists. It uses duck typing to handle different types of iterables.
"""

### 6. Using Duck Typing in Custom Classes
You can also create custom classes that utilize duck typing. For example:

class Dog:
    def bark(self):
        print("Woof!")
class Cat:
    def meow(self):
        print("Meow!")
def make_noise(animal):
    if hasattr(animal, 'bark'):
        animal.bark()
    elif hasattr(animal, 'meow'):
        animal.meow()
    else:
        print("Unknown sound")
dog = Dog()
cat = Cat()
make_noise(dog)  # Woof!
make_noise(cat)  # Meow!
"""
    In this example, `make_noise` checks for the presence of specific methods
    (`bark` and `meow`) and calls them if they exist. This is another form of
    duck typing where method existence is checked at runtime.
"""

### Conclusion
"""
    Duck typing in Python allows for more dynamic and flexible code by focusing on what an
    object can do rather than its specific type. This approach provides benefits like increased
    flexibility and code reusability but can also introduce potential runtime errors if not
    carefully managed. By understanding and leveraging duck typing, you can write more adaptable
    and powerful Python code.
"""