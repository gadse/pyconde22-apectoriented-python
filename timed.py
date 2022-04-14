"""We wanna time a function!"""

import functools as ft
from timeit import default_timer

MEASURE_TIME = False


def variably_timed(run_count: int):
    if run_count < 1:
        raise ValueError("run_count must be positive")

    if not MEASURE_TIME:
        run_count = 1

    def timed(func):
        "Decorates a function and prints its runtime every it's called."
        runs = []

        @ft.wraps(func)
        def _timed(*args, **kwargs):
            for i in range(run_count):
                start = default_timer()
                result = func(*args, **kwargs)
                duration = default_timer() - start
                runs.append(duration)
            if MEASURE_TIME:
                print(runs)
            print(MEASURE_TIME * f"execution time = {sum(runs) / len(runs)} seconds ({len(runs)} runs.)")
            return result
        return _timed

    return timed


@variably_timed(10)
def add(a, b):
    "I am a docstring."
    return a + b

if __name__ == "__main__":
    print(add(1,2))
    print(add.__doc__)