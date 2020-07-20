
# decorator approach


def singleton_decorator(cls):
    _instance = {}

    def util():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return util


@singleton_decorator
class SingletonOne:

    def print_id(self):
        print(id(self))

# -----------------------------

# __new__ approach


class SingletonTwo(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def print_id(self):
        print(id(self))

# -----------------------------

#  metaclass approach


class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class SingletonThree(metaclass=MetaSingleton):
    def print_id(self):
        print(id(self))


if __name__ == "__main__":
    product_a = SingletonOne()
    product_b = SingletonOne()
    product_a.print_id()
    product_b.print_id()

    product_a = SingletonTwo()
    product_b = SingletonTwo()
    product_a.print_id()
    product_b.print_id()

    product_a = SingletonThree()
    product_b = SingletonThree()
    product_a.print_id()
    product_b.print_id()