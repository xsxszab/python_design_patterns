
from abc import ABC, abstractmethod


class AbcComponent(ABC):

    @abstractmethod
    def visit(self, visitor):
        pass


class ComponentA(AbcComponent):

    def __init__(self):
        self.num = 1

    def visit(self, visitor):
        visitor.visit_a(self)


class ComponentB(AbcComponent):

    def __init__(self):
        self.num = 2

    def visit(self, visitor):
        visitor.visit_b(self)


class ComponentC(AbcComponent):

    def __init__(self):
        self.num = 3

    def visit(self, visitor):
        visitor.visit_c(self)


class Product:
    def __init__(self, comp_a: ComponentA, comp_b: ComponentB, comp_c: ComponentC):
        self.a = comp_a
        self.b = comp_b
        self.c = comp_c

    def visit(self, visitor):
        print('visit entire product')
        self.a.visit(visitor)
        self.b.visit(visitor)
        self.c.visit(visitor)


class Visitor:

    def visit_a(self, instance):
        print(f'visit a, value: {instance.num}')

    def visit_b(self, instance):
        print(f'visit b, value: {instance.num}')

    def visit_c(self, instance):
        print(f'visit c, value: {instance.num}')


if __name__ == "__main__":
    component_a = ComponentA()
    component_b = ComponentB()
    component_c = ComponentC()
    product = Product(component_a, component_b, component_c)

    visitor = Visitor()
    product.visit(visitor)
