```bash
node -v # to verify installation
node # open the node interactive shell, it is called Node REPL as it READ js code the user type EVALUATE the result of interpreting the line of code PRINT the output to use and LOOP unitll the user signaling to quit ctrl + C
```
**to run your js file using node:**
```bash
node fileName.js # or
node fileName
```

### Browser VS Nodejs

- in the browser most of the time what you are doing is interacting with the DOM or other Web Platform APIs like Cookies, but in node js you don't have the document, window and all the other objects that are provided by the browser
- in the browser we don't have all the nice APIs that Node js provides through its modules, for example the filesystem access functionality
- with node js you control the environment, you know your application dependencies version and all other needed libraries versions
- with a browser you are at the mercy of what the users choose e:g if he use internet explorer that means more work for us to do