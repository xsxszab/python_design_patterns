class Target(object):

    def request(self):
        print("target request")


class Adaptee(object):

    def specific_request(self):
        print("adaptee request")


class Adapter(Target):

    def __init__(self):
        self.adaptee = Adaptee()

    def request(self):
        self.adaptee.specific_request()


def user_code(obj_list: list):
    for item in obj_list:
        item.request()


if __name__ == "__main__":
    obj_list = []
    target_a = Target()
    target_b = Adapter()

    obj_list.append(target_a)
    obj_list.append(target_b)

    user_code(obj_list)
