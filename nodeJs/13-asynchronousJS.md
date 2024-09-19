### Asynchronous JS
- js in its most basic form, it is synchronous, blocking and single-threaded language
- **synchronous**: code execute top down with only one line executing at a time
- **blocking**: because of its synchronous nature, no matter how long a previous process takes, the subsequent process won't kick Off until the former is completed
- **single-threaded**: a thread is simply a process that you js program can use to run a task, each thread can only do one task at a time, js has only one thread (the main thread) to execute code

this synchronous behaviour is a problem, because let's say that you want to retreive some data from the database and doing some operation on the retreived data, you should wait for the data to be retreived first before moving on to the next line of code otherwise errors occur because data is not what we expect to be, with synchronous behaviour once the line of code that retreives data from database occur it will continue to the next line without waiting the data to come first which will create problems 

### **to add asynchronous behaviour to js**

- in frontEnd this is where <mark>web browsers</mark> come into play, and for the backEnd this is where <mark>Nodejs</mark> comes into play
- web browsers and nodejs define functions and APIs that allow us to register functions that should not be executed synchronously and should instead be invoked asynchronously when some kind of an event occurs
- e:g that could be the passage of time (setTimeout or setInterval), the user's interaction with the mouse (addEvnetListener), data being read from a file system or the arrival of data over the network (callBacks, promises, async-await)