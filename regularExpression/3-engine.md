### how regex engine works
Let's break down the matching process of the regular expression `a[bcd]*b` against the string `"abcbd"` step-by-step. This will help you understand how the regex engine works, especially when dealing with greedy quantifiers like `*`.

### Regular Expression Breakdown: `a[bcd]*b`

- **`a`**: Matches the character 'a'.
- **`[bcd]*`**: Matches zero or more characters from the set `[b, c, d]`. This is a *greedy* match, meaning it tries to match as many characters as possible.
- **`b`**: Matches the character 'b'.

### Step-by-Step Matching Process

1. **Initial Matching Attempt**
   - **Current Position**: Start of the string `"abcbd"`.
   - **Matched**: `"a"`
   - **Explanation**: The engine matches the first `a` in the pattern with the first character of the string.

2. **Greedy Matching `[bcd]*`**
   - **Current Position**: After matching `a`, the engine tries to match `[bcd]*` as far as it can.
   - **Matched**: `"abcbd"`
   - **Explanation**: `[bcd]*` tries to consume as much of the string as possible, so it matches all characters up to the end of the string.

3. **Matching the Final `b`**
   - **Current Position**: The engine is at the end of the string after the greedy match.
   - **Matched**: Failure
   - **Explanation**: The regex tries to match `b`, but it's already at the end of the string, so it fails.

4. **Backtracking Step 1**
   - **Current Position**: Back up one character.
   - **Matched**: `"abcb"`
   - **Explanation**: The engine reduces the match of `[bcd]*` by one character, leaving the last character `'d'` unmatched.

5. **Attempt to Match `b` Again**
   - **Current Position**: At the last character `'d'`.
   - **Matched**: Failure
   - **Explanation**: The current character is `'d'`, but the pattern expects a `b`, so it fails.

6. **Backtracking Step 2**
   - **Current Position**: Back up another character.
   - **Matched**: `"abc"`
   - **Explanation**: The engine reduces the match of `[bcd]*` further, now only matching `'bc'`.

7. **Successful Match of Final `b`**
   - **Current Position**: After matching `"abc"`, the engine now tries to match the final `b`.
   - **Matched**: `"abcb"`
   - **Explanation**: The current character is `'b'`, which matches the final `b` in the pattern, so the engine successfully matches the full pattern.

### Summary

- **Greedy Matching**: The engine initially matches as much as it can with `[bcd]*`.
- **Backtracking**: When it can't match the final `b`, it starts to backtrack, reducing the length of `[bcd]*` until it finds a match or exhausts all possibilities.
- **Final Match**: The engine stops when it successfully matches the entire pattern `a[bcd]*b` with `"abcb"`.

This example demonstrates how the regex engine works with greedy quantifiers (`*`). It first tries to match as much as possible and then backtracks if it can't match the rest of the pattern. This process continues until the pattern is fully matched or the engine concludes there's no match.