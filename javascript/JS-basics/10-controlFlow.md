### if condition (33-35)
```js
if (condition) {
    ...
} else if {
    ...
} else {
    ...
}
```

### Ternary operator
```js
let gender = 'm';
res = gender === 'm' ? 'male' : 'female';
 
age < 20
    ? dosomething
    : age > 20 && age < 60
    ? dosomething
    : age > 60
    ? dosomething
    : dosomethingIFallFalse
```

### switch (83)
- switch compares using identical operator ===
- so type and value should be equal
```js
let data = 0;
switch(day) {
    case 0:
        dosomeThing;
        break;
    case 1:
        doSOmething
        break;
    // case 2 and 3 have the same results
    case 2:
    case 3:
        // code of case 2 and 3
        break;
    // you can put default any where in the switch statement
    // but don't forget to include break if you put it any where except the end
    default:
        donsomthing
}
```