# Memoization
The term “Memoization” comes from the Latin word “memorandum” (to remember), which is commonly shortened to “memo” in American English, and which means “to transform the results of a function into something to remember.”.

In computing, memoization is used to speed up computer programs by eliminating the repetitive computation of results, and by avoiding repeated calls to functions that process the same input.

### Why is Memoization used?
Memoization is a specific form of caching that is used in dynamic programming. The purpose of caching is to improve the performance of our programs and keep data accessible that can be used later. It basically stores the previously calculated result of the subproblem and uses the stored result for the same subproblem. This removes the extra effort to calculate again and again for the same problem. And we already know that if the same problem occurs again and again, then that problem is recursive in nature.

### Where to use Memoization?
We can use the memoization technique where the use of the previously-calculated results comes into the picture. This kind of problem is mostly used in the context of <mark>recursion</mark>, especially with problems that involve overlapping subproblems.

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

### Ref
[GFG](https://www.geeksforgeeks.org/what-is-memoization-a-complete-tutorial/)