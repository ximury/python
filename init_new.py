class A(object):
    def __init__(self):
        print("This is init method: ", self)

    def __new__(cls):
        print("This is cls ID: ", id(cls))
        print("This is new method: ", object.__new__(cls))
        return object.__new__(cls)


A()
print("This is class A ID: ", id(A))
