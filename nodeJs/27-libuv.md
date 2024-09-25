### libuv
- is a cross platform open source library written in C language
- it handles asynchronous non-blocking operation in nodejs
- it does that by using Tread Pool and Event loop

### Thread Pool
- there is a conversation between js main thread and libuv when main thread encounters an asynchronous operation.
- libuv has a pool of threads that can run some of these time consuming tasks, when the task is done the file contents are retrieved and the associated callback function can be run
- libuv thread pool has 4 threads in total (4 async operation at a time)
- you can increase the pool size by setting process environmental variable
```js
process.env.UV_THREADPOOl_SIZE = 5
```
- watch [this](https://youtu.be/I1sqnbJ1Fno?si=SGW1DyF2AtVtu2lw) and [this](https://youtu.be/3JYNNf3Iljo?si=4Fbx7DLkXTq5QrHV)

## Event loop