# Monitoring setup (e.g., Prometheus or custom)import time
from functools import wraps

def monitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"[MONITOR] Function '{func.__name__}' took {duration:.2f} seconds.")
        return result
    return wrapper
