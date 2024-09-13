### Events
- the envents module allows us to work with events in node.js
- an <mark>event</mark> is an action or an occurrence that has happened in our application that we can respond to
- using the events module, we can dispatch our own custom events and respond to those custom events in a non-blocking manner

```js
const Event = require("node:events")
const emitter = new Event()
```
### emitting an event
- use <mark>emit<mark> method
- emit method accept <mark>eventName<mark> as an argument
```js
emitter.emit("order-pizza")
```