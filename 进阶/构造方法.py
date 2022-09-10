class Person:
    # 构造方法是用于初始化对象属性的方法：
    # 方法名的前缀和后缀是两个下划线 _
    # 方法的第一个参数 self 指向新创建的对象
    # 方法的其余参数用于设定对象的属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print('name = %s, age = %d' % (self.name, self.age))

    # 该方法在删除前被调用，该方法又被称为析构方法
    # 方法名的前缀和后缀是两个下划线 _
    # 方法的参数 self 指向将被删除的对象
    def __del__(self):
        print('del %s' % self.name)


tom = Person('tom', 10)
tom.introduce()

jerry = Person('jerry', 20)
jerry.introduce()

del tom
del jerry
