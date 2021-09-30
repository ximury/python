# 实例化一个单例
class Singleton(object):
    __instance = None

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance


# a, b是一个对象
a = Singleton(18, "LiMing")
b = Singleton(18, "Liming")

print(id(a))
print(id(b))

# 添加属性值
a.age = 19
print(b.age)
