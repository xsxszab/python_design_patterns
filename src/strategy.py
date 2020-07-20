
from abc import ABC, abstractmethod


class AbcStrategy(ABC):

    @abstractmethod
    def calc(self, num):
        pass


class StrategyA(AbcStrategy):

    def calc(self, num):
        res = num + 1
        print(f'algorithm A num: {res}')
        return res


class StrategyB(AbcStrategy):

    def calc(self, num):
        res = num + 2
        print(f'algorithm B num: {res}')
        return res


class Interface:

    def __init__(self, strategy: AbcStrategy):
        self.strategy = strategy

    def calc(self, num):
        return self.strategy.calc(num)

    def change_algorithm(self, strategy: AbcStrategy):
        self.strategy = strategy


if __name__ == "__main__":
    strategy_a = StrategyA()
    strategy_b = StrategyB()

    interface = Interface(strategy_a)
    interface.calc(10)
    interface.change_algorithm(strategy_b)
    interface.calc(10)
