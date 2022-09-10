# 1.通过复杂的推导创建生成器
generator = (i for i in range(10) if i % 2 == 0)
for i in generator:
    print(i, end='-')
print()


# 2.通过 yield 创建生成器
def generateOddNumbers(n):
    for i in range(n):
        if i % 2 == 1:
            yield i


generator = generateOddNumbers(10)
for i in generator:
    print(i, end='--')
print()


# 3.堆栈
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


def stackGenerate(stack):
    cursor = stack.head
    while cursor is not None:
        yield cursor.item
        cursor = cursor.next


stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')

# 通过 while 循环遍历堆栈
generator = stackGenerate(stack)
while True:
    try:
        item = next(generator)
        print(item, end='---')
    except StopIteration:
        break
print()
# 通过 for … in 循环遍历堆栈
generator = stackGenerate(stack)
for item in generator:
    print(item, end='----')
print()


# 4.实现统计文本中单词
def generateWord(file):
    while True:
        line = file.readline()
        if not line:
            break

        words = line.split()
        for word in words:
            yield word


file = open('word.txt')
count = 0
dic = {}
for word in generateWord(file):
    count = count + 1
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
print("total: {} words".format(count))

for word, count in dic.items():
    print('{}: {}'.format(word, count))
