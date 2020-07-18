
from abc import ABC, abstractmethod


class AbcHandler(ABC):

    @abstractmethod
    def handle(self, request: str):
        pass

    @abstractmethod
    def set_next(self, handler):
        pass


class BaseHandler(AbcHandler):

    def __init__(self):
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, request: str):
        if self._next:
            return self._next.handle(request)
        return None


class HandlerA(BaseHandler):

    def handle(self, request: str):
        if request == 'A' or request == 'a':
            return 'handle a'
        else:
            return super().handle(request)


class HandlerB(BaseHandler):
    def handle(self, request: str):
        if request == 'B' or request == 'b':
            return 'handle b'
        else:
            return super().handle(request)


class HandlerC(BaseHandler):
    def handle(self, request: str):
        if request == 'C' or request == 'c':
            return 'handle c'
        else:
            return super().handle(request)


if __name__ == "__main__":
    handle_a = HandlerA()
    handle_b = HandlerB()
    handle_c = HandlerC()
    handle_a.set_next(handle_b).set_next(handle_c)

    print(handle_a.handle('a'))
    print(handle_a.handle('b'))
    print(handle_a.handle('c'))
