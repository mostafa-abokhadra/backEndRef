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


```py

```
# Ref
- [corey] (https://www.youtube.com/watch?v=-ARI4Cz-awo)