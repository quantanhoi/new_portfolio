import signal
from functools import wraps
from flask import jsonify

class TimeoutException(Exception):
    pass

def timeout(seconds=10, error_message="API request timed out"):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutException(error_message)

        @wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wrapper
    return decorator


def handle_timeout_error(e):
    return jsonify(error=str(e)), 408
