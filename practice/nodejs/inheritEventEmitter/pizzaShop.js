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