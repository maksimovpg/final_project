import typing
from random import randint


def log(format_string: str):
    """
    Creates a decorator that return a formatted message
    using format string.

    :param format_string: format string where a random number will be inserted
    when the function is called.
    :return: decorator function that adds logging
    """

    def decorator(func: typing.Callable):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            print(format_string.format(randint(5, 20)))
            return res

        return wrapper

    return decorator
