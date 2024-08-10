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