

class Mediator:

    def __init__(self):
        self.component_list = []

    def bind(self, component):
        self.component_list.append(component)
        component.set_mediator(self)

    def send(self, msg: str, idx: int):
        for item in self.component_list:
            if item.num == idx:
                item.receive(msg)


class Component:

    def __init__(self, num):
        self.num = num
        self.mediator = None

    def send(self, msg, idx):
        if not self.mediator:
            return
        print(f'component {self.num} sent message: {msg}')
        self.mediator.send(msg, idx)

    def receive(self, msg):
        print(f'component {self.num} received message: {msg}')

    def set_mediator(self, mediator):
        self.mediator = mediator


if __name__ == "__main__":
    component_a = Component(1)
    component_b = Component(2)
    component_c = Component(3)

    mediator = Mediator()
    mediator.bind(component_a)
    mediator.bind(component_b)
    mediator.bind(component_c)

    component_a.send('a', 2)
    component_b.send('b', 3)
    component_c.send('c', 1)
