# Memoization

Memoization is an optimization technique used in computing to improve the performance of functions by caching the results of expensive function calls and reusing those results when the same inputs occur again. This can significantly reduce the time complexity of algorithms, especially those that involve recursive calculations or repeated function calls with the same parameters.

### How Memoization Works

1. **Function Call**: When a function is called with a specific set of parameters, the function computes its result.
  
2. **Caching the Result**: Before returning the result, the function stores this result in a cache (a data structure like a dictionary) with the function's input parameters as the key.

3. **Subsequent Calls**: If the function is called again with the same parameters, instead of recomputing the result, it retrieves the result directly from the cache.

4. **Return Cached Result**: The cached result is returned immediately, bypassing the need for recalculating.

### Benefits of Memoization

- **Efficiency**: By avoiding redundant calculations, memoization can greatly improve the runtime of algorithms, particularly in cases of overlapping subproblems, such as in dynamic programming.

- **Time Complexity Reduction**: For example, in recursive algorithms like computing Fibonacci numbers, memoization can reduce an exponential time complexity to linear time.

### Example: Fibonacci Sequence with and without Memoization

#### Without Memoization

The Fibonacci sequence is a classic example where memoization can be beneficial. Consider a naive recursive implementation:

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

- **Time Complexity**: The time complexity of this naive approach is \(O(2^n)\) because it recalculates the same Fibonacci numbers multiple times.

#### With Memoization

By adding memoization, we can store the results of Fibonacci numbers that have already been computed:

```python
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

- **Time Complexity**: With memoization, the time complexity reduces to \(O(n)\) because each Fibonacci number is computed only once.

### Using Python's `functools.lru_cache` for Memoization

Python's `functools` module provides a built-in way to apply memoization through the `lru_cache` decorator, which stands for "Least Recently Used" cache. It automatically caches the results of function calls and can manage the cache size.

```python
from functools import lru_cache

@lru_cache(maxsize=None)  # maxsize=None means the cache can grow indefinitely
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

- **Cache Size**: The `maxsize` parameter controls the number of cached results. If `maxsize` is set to `None`, the cache can grow without bound; otherwise, the least recently used items are discarded when the cache is full.

- **Advantages**: This approach is concise and leverages Python's built-in tools, making it easier to manage and apply memoization without manually implementing the cache logic.

### Manual Memoization

You can also manually implement memoization using a dictionary or another data structure:

```python
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
        
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

- **Flexibility**: Manual memoization gives you full control over the caching logic and can be adapted for more complex scenarios where you need to customize cache behavior.

### Considerations

- **Memory Usage**: While memoization speeds up function calls, it also consumes memory because the results are stored in the cache. In cases with very large inputs or a vast number of unique calls, this could lead to high memory usage.

- **Applicability**: Memoization is most effective for functions where the same inputs are likely to occur multiple times and the computation is costly. It’s less useful for functions with highly variable inputs or where the computation is relatively cheap.

- **Cache Invalidation**: In long-running programs, you might need to manage the cache, clearing it at appropriate times to free up memory. This is particularly relevant in web applications or systems with dynamic data.

### Summary

Memoization is a powerful technique in Python that improves the performance of functions by caching and reusing the results of previous computations. It is particularly useful in recursive algorithms and dynamic programming, where the same calculations are performed multiple times. Python's `functools.lru_cache` provides an easy-to-use implementation for memoization, but you can also implement it manually when needed. However, while memoization can significantly reduce time complexity, it comes with the trade-off of increased memory usage.

___
```py
def memoize(fn: Callable) -> Callable:
    """Decorator to memoize a method.
    Example
    -------
    class MyClass:
        @memoize
        def a_method(self):
            print("a_method called")
            return 42
    >>> my_object = MyClass()
    >>> my_object.a_method
    a_method called
    42
    >>> my_object.a_method
    42
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """"memoized wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)
```

The code provided is a Python decorator function named `memoize`. This decorator is designed to cache the result of a method in a class, so that subsequent calls to the method return the cached result instead of recalculating it. Let's break down the code in detail.

### Code Breakdown


#### **Setting Up the Cache Attribute**

```python
attr_name = "_{}".format(fn.__name__)
```

- **`attr_name`**: This line creates a string that will be used as the name of the attribute where the result of the method will be cached. The attribute name is derived from the original method's name (`fn.__name__`), prefixed with an underscore (`_`). This helps to avoid naming conflicts with other attributes.

#### 4. **Defining the Memoized Wrapper Function**

```python
@wraps(fn)
def memoized(self):
    """memoized wraps"""
    if not hasattr(self, attr_name):
        setattr(self, attr_name, fn(self))
    return getattr(self, attr_name)
```

- **`@wraps(fn)`**: This is a decorator from the `functools` module. It ensures that the `memoized` function retains the metadata (like the docstring and name) of the original function `fn`. This is useful for debugging and documentation purposes.

- **`def memoized(self):`**: The `memoized` function is the actual function that will replace the original method when the `memoize` decorator is applied. This function is responsible for checking if the result is already cached, and if not, it calculates and caches it.

- **`if not hasattr(self, attr_name):`**: This checks if the object (`self`) already has an attribute with the name `attr_name`. If the attribute does not exist, it means the method hasn't been called before, and the result isn't cached.

- **`setattr(self, attr_name, fn(self))`**: If the result is not cached, this line calls the original method (`fn(self)`), stores its result in the attribute named `attr_name` on the object, and effectively caches it.

- **`return getattr(self, attr_name)`**: Whether the result was cached or just computed, this line returns the cached value. The `getattr` function retrieves the value of the attribute named `attr_name` from the object (`self`).

#### 5. **Returning a Property Object**

```python
return property(memoized)
```

- **`property(memoized)`**: This converts the `memoized` function into a property of the class. When the decorated method is accessed (e.g., `my_object.a_method`), it invokes the `memoized` function rather than directly calling the original method. This way, the method behaves like an attribute of the class, but its value is computed lazily and cached on the first access.

### Example Explained

The example in the docstring demonstrates how the `memoize` decorator is used:

```python
class MyClass:
    @memoize
    def a_method(self):
        print("a_method called")
        return 42
```

- **First Access**:
  - When `my_object.a_method` is accessed for the first time:
    - `memoized` checks if `_a_method` is already an attribute of `my_object`. 
    - Since it's not, it calls `a_method` (which prints "a_method called" and returns `42`).
    - The result `42` is stored as `_a_method` in `my_object`.
    - `42` is returned.

- **Subsequent Access**:
  - The next time `my_object.a_method` is accessed:
    - `memoized` finds `_a_method` in `my_object` and directly returns its value (`42`) without calling `a_method` again.
    - No print statement is executed because the method is not re-evaluated.

### Summary

- **Memoization**: The decorator caches the result of a method the first time it is called and returns the cached result for subsequent calls, improving performance.
- **Usage**: This technique is particularly useful for methods whose results do not change over time and are expensive to compute.
- **Property**: By returning a property object, the decorated method behaves like a lazily evaluated attribute, making it easy to work with in Python classes.


The line `return property(memoized)` in the `memoize` decorator is crucial for how the decorated method behaves when accessed. Let's break it down in more detail.

### `property` in Python

In Python, the `property()` function is used to create managed attributes (also known as properties). A property allows you to control access to a class attribute by defining methods for getting, setting, and deleting the attribute's value. Properties are a way to customize access to instance attributes while maintaining a clean and intuitive interface for the user of the class.

#### Basic Example of `property`

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print("Getting value")
        return self._value

    @value.setter
    def value(self, new_value):
        print("Setting value")
        self._value = new_value

obj = MyClass(10)
print(obj.value)  # Getting value, 10
obj.value = 20    # Setting value
```

In this example, `value` is a property that controls access to the `_value` attribute. The `@property` decorator turns the `value` method into a getter, allowing `obj.value` to access `_value` while also printing a message.

### `property(memoized)`

Now, back to your code:

```python
return property(memoized)
```

This line converts the `memoized` function into a property of the class. Here's what happens:

1. **Turning a Method into a Property**:
   - Normally, when you define a method in a class, you call it like `obj.method()`.
   - By returning `property(memoized)`, you're transforming the `memoized` function into a property. This means you no longer need to use parentheses to call it; you access it like an attribute: `obj.a_method`.

2. **Lazy Evaluation**:
   - The first time you access `obj.a_method`, the `memoized` function is invoked. It checks if the result of `a_method` has already been cached in the `_a_method` attribute.
   - If not cached, `memoized` calls the original method `a_method`, caches the result, and returns it.
   - On subsequent accesses, `memoized` directly returns the cached value from `_a_method` without recalculating it.

3. **Simplified Syntax**:
   - The use of `property` simplifies the syntax for the user of the class. Instead of calling `obj.a_method()`, they can just write `obj.a_method`, which makes the code cleaner and easier to read.
   - It also gives the appearance that `a_method` is a regular attribute, even though it’s computed dynamically and cached.

4. **Immutable Property**:
   - Since the `property` is defined with only a getter (`memoized`), it is effectively read-only. Users can access the cached value but cannot modify it directly, preserving the integrity of the cached data.

### Detailed Example

Consider this class using the `memoize` decorator:

```python
class MyClass:
    @memoize
    def a_method(self):
        print("Computing...")
        return 42

obj = MyClass()

# First access
print(obj.a_method)  # Output: "Computing...", 42

# Second access
print(obj.a_method)  # Output: 42
```

- **First Access (`obj.a_method`)**:
  - `memoized` is invoked.
  - It checks if `_a_method` exists in `obj`. It doesn’t, so `a_method` is called.
  - `"Computing..."` is printed, and `42` is returned and stored in `_a_method`.
  - The result `42` is returned.

- **Second Access (`obj.a_method`)**:
  - `memoized` is invoked again.
  - This time, `_a_method` exists in `obj`, so `memoized` directly returns `42` without calling `a_method` again.

### Summary

The line `return property(memoized)` in the `memoize` decorator makes the decorated method behave like a property of the class:

- **Access**: The method is accessed like an attribute, not a function call.
- **Lazy Evaluation**: The method is evaluated and cached on the first access, and subsequent accesses return the cached value.
- **Simplified Interface**: It creates a clean and simple interface for the user of the class, making the method appear like a regular attribute.


### Ref
[GFG](https://www.geeksforgeeks.org/what-is-memoization-a-complete-tutorial/)