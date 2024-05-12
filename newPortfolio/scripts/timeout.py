import time
from functools import wraps

def timeout(seconds=10, error_message="Timeout"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            if end - start > seconds:
                raise TimeoutError(error_message)
            return result
        return wrapper
    return decorator
