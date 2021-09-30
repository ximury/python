
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


my_class = MyNumbers()

my_iter = iter(my_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
