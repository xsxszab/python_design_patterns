
from typing import List
from abc import ABC, abstractmethod


class AbcDevice(ABC):

    @abstractmethod
    def operation(self):
        pass


class DeviceA(AbcDevice):

    def operation(self):
        print('operation a')


class DeviceB(AbcDevice):

    def operation(self):
        print('operation b')


class Facade:
    def __init__(self, dev_list: List[AbcDevice]):
        self.dev_list = dev_list

    def operation(self):
        for item in self.dev_list:
            item.operation()


if __name__ == "__main__":
    devs = [DeviceA(), DeviceA(), DeviceB()]
    facade = Facade(devs)
    facade.operation()
