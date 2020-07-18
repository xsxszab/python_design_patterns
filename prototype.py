
import copy


class Component:

    def __init__(self, integer, lst):
        self.integer = integer
        self.lst = lst

    def __copy__(self):
        lst = copy.copy(self.lst)
        new_instance = self.__class__(self.integer, lst)
        return new_instance

    def __deepcopy__(self, memo={}):
        lst = copy.deepcopy(self.lst)
        new_instance = self.__class__(self.integer, lst)
        return new_instance


if __name__ == "__main__":
    lst = [['a', 'b'], 1, 2, 3]
    old_component = Component(1, lst)
    new_component_1 = copy.copy(old_component)
    new_component_2 = copy.deepcopy(old_component)
    print(f'{id(old_component.lst)}  {id(new_component_1.lst)}')
    print(f'{id(old_component.lst[0])}  {id(new_component_1.lst[0])}')
    print(f'{id(old_component.lst[0])}  {id(new_component_2.lst[0])}')
