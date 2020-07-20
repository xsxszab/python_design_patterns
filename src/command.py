
from abc import ABC, abstractmethod


class AbcCommand(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class CommandA(AbcCommand):

    def __init__(self, num: int):
        self.num = num

    def execute(self) -> None:
        print(f'command a num: {self.num}')


class CommandB(AbcCommand):

    def __init__(self, processer, num_a: int, num_b: int):
        self.processer = processer
        self.num_a = num_a
        self.num_b = num_b

    def execute(self) -> None:
        print(f'command b num: {self.num_a} {self.num_b}')
        self.processer.process(self.num_a, self.num_b)


class Processer:

    def process(self, num_a: int, num_b: int):
        print(f'{num_a} + {num_b} = {num_a + num_b}')


class Invoker:

    def __init__(self):
        self._on_start_command = None
        self._on_finish_command = None

    def set_on_start_command(self, command: AbcCommand):
        self._on_start_command = command

    def set_on_finish_command(self, command: AbcCommand):
        self._on_finish_command = command

    def do_something(self):
        self._on_start_command.execute()
        print('invoker is running')
        self._on_finish_command.execute()


if __name__ == '__main__':
    command_a = CommandA(1)
    command_b = CommandB(Processer(), 2, 4)
    invoker = Invoker()
    invoker.set_on_start_command(command_a)
    invoker.set_on_finish_command(command_b)
    invoker.do_something()
