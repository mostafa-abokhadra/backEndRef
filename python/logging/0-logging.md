### logging
- it is a means of tracking events that happen when some software runs.
- we adds logging calls to their code to indicate that certain events have occurred
- An event is described by a descriptive message which can optionally contain variable data (i.e. data that is potentially different for each occurrence of the event). Events also have an importance which the developer ascribes to the event; the importance can also be called the level or severity.

```py
# logger levels
"""
    debug()
    info()
    warning() # default level
    error()
    critical()
"""
import logging
# myLogger = getLogger(__name__)
logging.basicConfig(filename='myFile.log', level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s")
# the default level is warning meaning that only warnings and below function e:i error() and critical() will be logged
# so to change the level we use tha attribute level=logging.DEBUG
# or whatever level you want
logging.debug("some message")
# if you tried this before setting the level to logging.DEBUG, it won't work
# will print the log message to the console
# if you want to log you messages in a file instead specify the 
# file name attribute in basicConfig
"""
    format: change the message format, the default looks like something like this:
        LevelName:logger:message e:g
        DEBUG:root:some message
    the above format code will change default format to be something like this:
        data-time:levleName:the message
    the loggger "root" because we don't actually specified a specific logger so it use
        root as default, but best practice is to specify a logger for each module
"""
```

check all of the `format` basicConfig attribute formats in this [link](https://docs.python.org/3/library/logging.html#logrecord-attributes)

###### why is it not a goog idea to use the root logger or to use the same logger for all modules
let's say that you have two modules, module1.py and module2.py, in both modules you implemented the root logger basicCofiguration as follow
```py
# module1.py
logging.basicConfig(filename="file1.log", level=logging.DEBUG)
# module2.py
logging.basicConfig(filename="file2.log", level=logging.INFO)
```
then in module1 you import module2, here is what will happen:

when you import a module its code actually runs when you import it, so root logger basicConfig will be as one in the module2.py because it is the first to run, and when you reach logging.basciConfig line in module1.py it will not override the preset basicConfig from the imported module
so all of your log statements that in module1.py will not get logged in the file1.log or even file2.log because it's level is higher that the preset level in module2.py e:i level=logging.INFO
but for example if you changed your log statements in module1.py to use INFO instead of DEBUG it will get logged in file2.log

### to create a new logger
```py
import logging

myLogger = logging.getLogger(__name__)
# you can actully specify any name you want instead of __name__, but the convention to use __name__
# now you can use this logger to run your logging methods instead of using the module name 'logging'itself which will runs the root logger not your new logger

myLogger.info("message") # not logging.info()

# to set the logger level
myLogger.setLevel(logging.INFO)

# to put your new logger messages in a file you should create a filehandler
myFileHandler = logging.fileHandler('file.log')
myLogger.addHandler(myFileHandler)

# to specify a new format, you create new formater and pass to the filehandler
myFromatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
myFileHandler.setFormatter(myFormatter)

# if you want only a specific level to get logged in your file you can setLevel for you file handler
myFileHandler.setLevle(logging.ERROR)

def divison(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        logger.error("tried To Divide By Zero")
        # or if you want to include the trace back message
        # use logger.excption()
        logger.exception("a message")
    else:
        return result

    """
        you can create multiple handler to a logger, for example the example above uses the file handler to log all error messages to a file, let's say now that you wnat to display all debug messages to the console you can add a stream handler
    """
    myStreamHandler = logging.streamHandler()
    # you can also add the formatter to the stream handler
    myStreamHandler.setFromatter(myFormatter)
    logger.addHandler(myStreamHandler)
    # this will actually print debug messages and also error messages in the console but will also log erro message in the file
```

# Ref
- [corey] (https://www.youtube.com/watch?v=-ARI4Cz-awo)
- [coreyPart2](https://www.youtube.com/watch?v=jxmzY9soFXg)