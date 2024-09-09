# NodeJS

- **open source:** source code is publicly available for sharing and modification
- **cross platform:** available on Mac, windows and linux
- **javascript runtime environment**: ?
- it builds end-to-end js application

### ECMA SCRIPT stroy
- list to the story and the difference between ECMAscript and js[here](https://youtu.be/HXpPKhWOkAs?si=8LoZL3M57CzPTIpo)

### JS engine
- it is the program that converts js code to the machine code, each browser has it's own engine
- **V8** is the engine developed by google for chrome
- **spidermonkey** developed by mozilla for firefox
- **jsCore** developed by apple for safari
- **chakra** for microsoft edge (now uses V8)

> [!NOTE]
> V8 engine is written using C++, so you can embed V8 engine in your C++ application
> you can write C++ code that get executed when the user write js code, in other words you can add new features for js itself

> [!TIP]
> - since C++ is great for lower level operations like file handling, database conncetions and network operations, by embedding V8 into your own C++ program you have the power to add all of that functionaliy in js
> - the C++ program we're talking about is nothing but Node js
