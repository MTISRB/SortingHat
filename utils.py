from functools import wraps


def sort(ds, data: str, d_id: str) -> list:
    sorted_list = [[] for _ in range(15)]

    try:
        for x in ds:
            if isinstance(x, dict):
                for i, d in enumerate(x.values()):
                    sorted_list[int(d[d_id])].append(d[data])
    except IndexError:
        traceback.format_exc()
    except KeyError:
        traceback.format_exc()

    return sorted_list


def memoize(func):
    r"""
    Any computation that uses recursive functions or functions that need to compute numbers over and over again,
    will be significantly faster with the help of this decorator.
    """

    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper
