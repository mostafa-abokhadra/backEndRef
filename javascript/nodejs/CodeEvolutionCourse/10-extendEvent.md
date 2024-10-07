### building a moudule on top of EventEmitter class
https://youtu.be/UK2uQjgsoI4?si=rX1dM7O4cdEgQw5y

```js
// paizzaShop.js
const EventEmitter = require('node:events');

class pizzaShop extends EventEmitter{

    constructor(){
        super()
        this.orderNumber = 0
    }
    order(size, type) {
        this.orderNumber++
        this.emit("orderPizza", size, type);
    }
    displayOrder(){
        return `your order number is ${this.orderNumber}`;
    }
}

module.exports = pizzaShop;
```

```js
// index.js
const pizzaShop = require('./pizzaShop');

const pizza = new pizzaShop();

function displayPizza(size, type)  {
    console.log(`paking ${size} ${type} pizza...`);
}

pizza.on("orderPizza", displayPizza)

pizza.order("large", "margareta")

console.log(pizza.listeners("orderPizza"))

console.log(`afterOrder: ${pizza.displayOrder()}`);
```
> [!TIP]
> - listeners("eventName") returns a list of all listeners of an event
> - console.log(pizza.listeners("orderPizza"))
