class A:
    def __init__(self, value: float):
        self.value = value


class B:
    def __init__(self, value: float):
        self.value = value


class ObjectException(Exception):
    ...


def func(obj):
    if isinstance(obj, A):
        print(obj.value)
    elif isinstance(obj, B):
        raise ObjectException("B object")
    else:
        print(obj)


func(A(10))
func(B(1.5))
func("hello!")
