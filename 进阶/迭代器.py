# -----------------1-----------------
iterable = []
for item in iterable:
    print(item)
# 即
iterator = iter(iterable)
while True:
    try:
        item = next(iterator)
        print(item)
    # 当迭代器遍历完全部元素后，抛出一个特殊的异常 StopIteration，表示迭代结束
    except StopIteration:
        break


# -----------------2-----------------
# 实现一个自定义的迭代器
# 通过单链表实现堆栈
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node


stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')
print(stack.head.__dict__.get('next').__dict__)


# -----------------3-----------------
# 迭代器实现统计文本中单词
# 类 IterateWord 既是可迭代对象也是迭代器:
# 类 IterateWord 是可迭代对象，提供了 __iter__ 方法，返回一个迭代器
# 类 IterateWord 是迭代器，提供了 __next__ 方法，返回下一个遍历的对象
class IterateWord:
    def __init__(self, file):
        self.file = file
        self.words = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.words) == 0:
            self.get_non_blank_line()
        word = self.words.pop(0)
        return word

    def get_non_blank_line(self):
        while True:
            line = self.file.readline()
            if not line:
                raise StopIteration
            self.words = line.split()
            if len(self.words) != 0:
                break


file = open('word.txt')
count = 0
dic = {}

for word in IterateWord(file):
    print(word)
    count = count + 1
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
print(count)

for word, count in dic.items():
    print('{}: {}'.format(word, count))
