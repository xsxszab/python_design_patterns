

def func_decorator(n: int):
    def inner_decorator(func):
        print(f'decorate parameter: {n}')

        def util(*args, **kwargs):
            print('execute start')
            ret = func(*args, **kwargs)
            print('execute end')
            return ret

        return util
    return inner_decorator


@func_decorator(10)
def print_msg(n: int, dic: dict) -> None:
    print('-' * 20)
    print(f'number: {n}')
    print(f'dict: {dic}')
    print('-' * 20)


class ClsDecorator:

    def __init__(self, func):
        print('cls decorator')
        self.func = func

    def __call__(self, *args, **kwargs):
        print('execute')
        return self.func(*args, **kwargs)


@ClsDecorator
def print_something():
    print('something')


if __name__ == "__main__":
    print_msg(1, {'one': 1})
    print_msg(2, {'two': 2})

    print()

    print_something()
    print_something()