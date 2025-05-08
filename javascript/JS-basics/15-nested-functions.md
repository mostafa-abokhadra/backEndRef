# Nested functions

We use **nested functions** (functions inside other functions) in programming for several important reasons:  

### 1. **Encapsulation & Scope Control**  
   - Nested functions can access variables from their parent function (**closures**), but they aren’t exposed to the outer scope.  
   - This helps avoid naming conflicts and keeps code modular.  

   **Example:**  
   ```javascript
   function outer() {
       const message = "Hello";
       function inner() {
           console.log(message); // Accesses 'message' from outer()
       }
       inner();
   }
   outer(); // Output: "Hello"
   ```

### 2. **Helper Functions**  
   - If a function is only needed within another function, nesting it keeps the code organized and avoids clutter in the global scope.  

   **Example:**  
   ```javascript
   function calculateDiscount(price) {
       function applyTax(amount) { // Only relevant inside calculateDiscount
           return amount * 1.1; // Adds 10% tax
       }
       const discounted = price * 0.9; // 10% discount
       return applyTax(discounted); // Reuse the nested function
   }
   console.log(calculateDiscount(100)); // Output: 99 (90 + 10% tax)
   ```

### 3. **Closures for State Preservation**  
   - Nested functions "remember" their parent’s variables even after the parent function finishes. This is useful for callbacks, event handlers, or factories.  

   **Example:**  
   ```javascript
   function counter() {
       let count = 0;
       return function() { // Nested function
           count++;
           return count;
       };
   }
   const increment = counter();
   console.log(increment()); // 1
   console.log(increment()); // 2 (remembers 'count')
   ```

### 4. **Avoiding Repetition**  
   - If a piece of logic is repeated inside a function but nowhere else, a nested function can make the code DRY (Don’t Repeat Yourself).  

### 5. **Callback Patterns**  
   - Nested functions are often used in asynchronous operations (e.g., `setTimeout`, `Promise`, event listeners) to handle logic with access to the parent’s scope.  

   **Example:**  
   ```javascript
   setTimeout(function() { // Anonymous nested function
       console.log("Delayed log");
   }, 1000);
   ```

### When **Not** to Use Nested Functions:  
   - If the nested function is reused elsewhere, define it separately.  
   - Deep nesting can make code harder to read (avoid "pyramid of doom").  

### Summary:  
Nested functions are powerful for **organization**, **privacy**, and **closures**, but use them judiciously to keep code clean.  
