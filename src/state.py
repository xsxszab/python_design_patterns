
from abc import ABC, abstractmethod


class Context:

    _state = None

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        self._state = state
        self._state.context = self

    def request_a(self):
        self._state.handle_a()

    def request_b(self):
        self._state.handle_b()


class AbcState(ABC):

    def __init__(self):
        self._context = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, cxt):
        self._context = cxt

    @abstractmethod
    def handle_a(self):
        pass

    @abstractmethod
    def handle_b(self):
        pass


class StateA(AbcState):

    def handle_a(self):
        print('state a handle a')
        print('go to state b')
        self.context.transition_to(StateB())

    def handle_b(self):
        print('state a handle b')


class StateB(AbcState):

    def handle_a(self):
        print('state b handle a')

    def handle_b(self):
        print('state b handle b')
        print('go to state a')
        self.context.transition_to(StateA())


if __name__ == "__main__":
    context = Context(StateA())
    context.request_b()
    context.request_a()
    context.request_a()
    context.request_b()
