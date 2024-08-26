# Memoization
The term “Memoization” comes from the Latin word “memorandum” (to remember), which is commonly shortened to “memo” in American English, and which means “to transform the results of a function into something to remember.”.

In computing, memoization is used to speed up computer programs by eliminating the repetitive computation of results, and by avoiding repeated calls to functions that process the same input.

### Why is Memoization used?
Memoization is a specific form of caching that is used in dynamic programming. The purpose of caching is to improve the performance of our programs and keep data accessible that can be used later. It basically stores the previously calculated result of the subproblem and uses the stored result for the same subproblem. This removes the extra effort to calculate again and again for the same problem. And we already know that if the same problem occurs again and again, then that problem is recursive in nature.

### Where to use Memoization?
We can use the memoization technique where the use of the previously-calculated results comes into the picture. This kind of problem is mostly used in the context of <mark>recursion</mark>, especially with problems that involve overlapping subproblems.


### Ref
[GFG](https://www.geeksforgeeks.org/what-is-memoization-a-complete-tutorial/)