# loops (48-56)
for, while and do while

#### label
- it allows you to control the loops using break and continue statement
- the below example break the mainloop when j's value becomes 4
```js
mainloop: for(let i = 0; i < 10; i++) {
    nestedLoop: for(let j = 0; j < 5; j++) {
        if (j === 4) {
            break mainloop;
        }
    }
}

const products = ["iphone", "tv"]
const i = 0;
for (;;) {
    console.log(products[i])
    i++;
    if (i === products.length) break;
}
```
### while and do while
```js
while() {

}

do {

} while();
```