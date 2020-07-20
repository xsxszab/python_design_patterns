
class Iterator:
    def __init__(self, lst: list):
        self._iter_list = lst
        self.index = 0
        self.length = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.length:
            value = self._iter_list[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration()


if __name__ == "__main__":
    iterator = Iterator([1, 2, 3, 4, 5, 6, 7])
    print(list(iterator))
