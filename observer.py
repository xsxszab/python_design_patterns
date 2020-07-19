
from abc import ABC, abstractmethod


class AbcSubject(ABC):

    @abstractmethod
    def attach(self, observer) -> None:
        pass

    @abstractmethod
    def detach(self) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class SubjectA(AbcSubject):

    def __init__(self):
        self.state = set()
        self._observers = []

    def attach(self, observer) -> None:
        self._observers.append(observer)

    def detach(self) -> None:
        self._observers = self._observers[:-1]

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def add_state(self, state: int):
        self.state.add(state)

    def remove_state(self, state: int):
        if state in self.state:
            self.state.remove(state)

class AbcObserver(ABC):

    @abstractmethod
    def update(self, sub: AbcSubject):
        pass


class ObserverA(AbcObserver):

    def update(self, sub: SubjectA):
        if  1 in sub.state:
            print('observer a get msg 1')


class ObserverB(AbcObserver):

    def update(self, sub: SubjectA):
        if 2 in sub.state:
            print('observer b get msg 2')


if __name__ == '__main__':
    subject = SubjectA()
    subject.attach(ObserverA())
    subject.attach(ObserverA())
    subject.attach(ObserverB())

    subject.add_state(1)
    subject.add_state(2)
    subject.notify()

    subject.detach()
    subject.notify()

    subject.remove_state(1)
    subject.notify()
