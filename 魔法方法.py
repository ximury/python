class New_int(int):
    def __add__(self, other):
        return self.__sub__(other)


a = New_int(3)
b = New_int(1)

print(a + b)


class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{}.{}'.format(self.x, self.y)


print(P(3, 8))
