### libuv
- is a cross platform open source library written in C language
- it handles asynchronous non-blocking operation in nodejs
- it does that by using Tread Pool and Event loop

### Thread Pool
- there is a conversation between js main thread and libuv when main thread encounters an asynchronous operation.
- libuv has a pool of threads that can run some of these time consuming tasks, when the task is done the file contents are retrieved and the associated callback function can be run
```js

```

## Event loop