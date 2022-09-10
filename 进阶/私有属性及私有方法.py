# 在属性名称前加上前缀 __，表示该属性为私有属性

class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


tom = Person('tom')
# print(tom.__name) # 'Person' object has no attribute '__name'
tom.set_name('jerry')
print(tom.get_name())


# 使用私有属性解决问题
class Segment:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end
        self.__length = self.__end - self.__start

    def get_start(self):
        return self.__start

    def set_start(self, start):
        self.__start = start
        self.__length = self.__end - self.__start

    def get_end(self):
        return self.__end

    def set_end(self, end):
        self.__end = end
        self.__length = self.__end - self.__start

    def get_length(self):
        return self.__start

    def set_length(self, length):
        self.__length = length

    def show(self):
        print('start = %d, end = %d, length = %d' % (self.__start, self.__end, self.__length))


segment = Segment(10, 100)
segment.set_start(20)
segment.show()


# 在方法名称前加上前缀 __，表示该方法为私有方法

# 分析文本功能
class Parser:
    # __parse_word 是一个辅助方法，它用于实现方法 parse_string，不需要公开给外界调用，因此将它设定为私有方法
    def __parse_word(self, word):
        if word.isdigit():
            print('digit: %s' % word, end=', ')
        elif word.isalpha():
            print('alpha: %s' % word, end=', ')
        elif word == '=' or word == '+' or word == '-':
            print('operator: %s' % word, end=', ')

    def parse_string(self, string):
        words = string.split(' ')
        for word in words:
            self.__parse_word(word)


parser = Parser()
parser.parse_string('sum = sum + 100')
