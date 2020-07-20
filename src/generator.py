
from abc import ABC, abstractmethod


class AbcGenerator(ABC):

    @abstractmethod
    def get_final_product(self):
        pass

    @abstractmethod
    def add_part_a(self):
        pass

    @abstractmethod
    def add_part_b(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass


class Generator(AbcGenerator):

    def __init__(self):
        self._product = Product()

    def get_final_product(self):
        res = self._product
        self._product = Product()
        return res

    def add_part_a(self):
        self._product.add_component('a')

    def add_part_b(self):
        self._product.add_component('b')

    def cleanup(self):
        self._product = Product()


class Product:

    def __init__(self):
        self.components = []
        self.length = 0

    def add_component(self, component):
        self.components.append(component)
        self.length += 1

    def print_msg(self):
        print('-'*20)
        print(f'total components: {self.length}')
        print(' '.join(self.components))
        print('-'*20)

    def get_num(self):
        return self.length


def generate_type_a(generator: Generator) -> Product:
    generator.cleanup()
    generator.add_part_a()
    generator.add_part_a()
    generator.add_part_a()
    return generator.get_final_product()


def generate_type_b(generator: Generator) -> Product:
    generator.cleanup()
    generator.add_part_b()
    generator.add_part_b()
    generator.add_part_b()
    return generator.get_final_product()


if __name__ == "__main__":
    generator = Generator()
    product_a = generate_type_a(generator)
    product_b = generate_type_b(generator)
    product_a.print_msg()
    product_b.print_msg()
