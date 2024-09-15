#!/usr/bin/node

const pizzaShop = require('./pizzaShop');

const pizza = new pizzaShop();

function displayPizza(size, type)  {
    console.log(`paking ${size} ${type} pizza...`);
}

pizza.on("orderPizza", displayPizza)

pizza.order("large", "margareta")

console.log(pizza.listeners("orderPizza"))

console.log(`afterOrder: ${pizza.displayOrder()}`);