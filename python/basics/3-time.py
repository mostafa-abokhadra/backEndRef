import time
start_time = time.time() # current time
time.sleep(4) # it waites for 4 sec before executing next line of code
end_time = time.time()
elapsed_time = end_time - start_time # measuring execution time, use time.perf_counter() for higher precison
print(elapsed_time)
time.perf_counter()
"""
    returns the value (in fractional seconds) of a high-resolution performance counter.
    It's used to measure time intervals with a high degree of accuracy.
    provide the most precise time measurement available on the system.
    This makes it suitable for measuring small time intervals,
    like the execution time of a small block of code.
    Independent of System Time: Unlike time.time(), which can be affected by system clock changes
    (like daylight saving time adjustments), time.perf_counter() is immune to such changes.
"""