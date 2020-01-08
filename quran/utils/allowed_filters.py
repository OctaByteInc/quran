import functools


class FilterNotAllow(Exception):
    pass


def allowed_filters(include=None, exclude=None):
    def filter_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if include:
                if not any(k in include for k in kwargs.keys()):
                    raise FilterNotAllow(f'One of the filter is not allowed, Allowed filters are {include}')
            elif exclude:
                if any(k in exclude for k in kwargs.keys()):
                    raise FilterNotAllow(f'One of the filter is not allowed, filters must not be in {exclude}')
            return func(*args, **kwargs)
        return wrapper
    return filter_decorator
