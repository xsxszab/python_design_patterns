
class Proxy:

    def __init__(self, instance):
        self._instance = instance

    def func(self):
        return 0

    def __getattr__(self, item):
        return getattr(self._instance, item)


class Device:

    def __init__(self):
        self.num = 10

    def func(self):
        return self.num


if __name__ == "__main__":
    dev = Device()
    proxy = Proxy(dev)

    print(dev.func())
    print(proxy.func())
