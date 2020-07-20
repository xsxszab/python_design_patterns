
from abc import ABC, abstractmethod


class AbcProduct(ABC):

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def print_msg(self):
        pass


class ProductA1(AbcProduct):

    def __int__(self):
        self.value = 10

    def get_value(self):
        return self.value

    def print_msg(self):
        print('product A 1')


class ProductB1(AbcProduct):

    def __int__(self):
        self.value = 20
        self.size = 100

    def get_value(self):
        return self.value

    def get_size(self):
        return self.size

    def print_msg(self):
        print('product B 1')


class ProductA2(AbcProduct):

    def __int__(self):
        self.value = 30

    def get_value(self):
        return self.value

    def print_msg(self):
        print('product A 2')


class ProductB2(AbcProduct):

    def __int__(self):
        self.value = 100
        self.size = 40

    def get_value(self):
        return self.value

    def get_size(self):
        return self.size

    def print_msg(self):
        print('product B 2')


class AbcFactory(ABC):

    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class FactoryOne(AbcFactory):

    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()


class FactoryTwo(AbcFactory):

    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()


def user_code(factory: AbcFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    product_a.print_msg()
    product_b.print_msg()
    print('production finished')


if __name__ == "__main__":
    user_code(FactoryOne())
    user_code(FactoryTwo())
