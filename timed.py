"""We wanna time a function!"""

import functools
from timeit import default_timer

RUNTIMES = {}


def timed(func):
    "Decorates a function and prints its runtime every it's called."

    @functools.wraps(func)
    def _timed(*args, **kwargs):
        start = default_timer()
        result = func(*args, **kwargs)
        duration = default_timer() - start
        print(f"execution time = {duration} seconds")
        key = ".".join([func.__module__, func.__name__])
        if not RUNTIMES.get(key):
            RUNTIMES[key] = []
        RUNTIMES[key].append(duration)
        return result

    return _timed


@timed
def add(a, b):
    "I am a docstring."
    return a + b

if __name__ == "__main__":
    print(add(1,2))
    add(3, 2)
    add(3, 2)
    add(3, 2)
    add(3, 2)
    print(add.__doc__)
    print(RUNTIMES)