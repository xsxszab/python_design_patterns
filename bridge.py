
from abc import ABC, abstractmethod


class Abstraction:

    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        self.implementation.implemented_operation()


class AbcImplementation(ABC):

    @abstractmethod
    def implemented_operation(self) -> None:
        pass


class ImplementationA(AbcImplementation):

    def implemented_operation(self) -> None:
        print('implementation a')


class ImplementationB(AbcImplementation):

    def implemented_operation(self) -> None:
        print('implementation b')


def user_code(abstraction: Abstraction) -> None:
    abstraction.operation()


if __name__ == "__main__":
    implementation_a = ImplementationA()
    implementation_b = ImplementationB()

    abstraction_a = Abstraction(implementation_a)
    abstraction_b = Abstraction(implementation_b)

    user_code(abstraction_a)
    user_code(abstraction_b)

