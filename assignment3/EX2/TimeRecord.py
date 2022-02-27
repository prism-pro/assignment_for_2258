from timeit import default_timer as timer
from functools import wraps
def timefn(fn):  # decorator to  measure time
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = timer()
        result = fn(*args, **kwargs)
        # print(result)
        t2 = timer()

        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result, t2 - t1

    return measure_time