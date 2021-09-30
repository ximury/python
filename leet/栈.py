# 异常类
class StackUnderflow(ValueError):  # 栈下溢(空栈访问)
    pass


class SStack:
    def __init__(self):
        self._elems = []  # 使用list存储栈元素

    def is_empty(self):
        return self._elems == []

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()

    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]

class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, data):
        """
        进栈函数
        """
        self.stack.append(data)

    def pop(self):
        """
        出栈函数，
        """
        return self.stack.pop()

    def gettop(self):
        """
        取栈顶
        """
        return self.stack[-1]

if __name__ == '__main__':
    s = SStack()
    assert s.is_empty() is True
    # try:
    #     s.pop()
    # except StackUnderflow:
    #     print("StackUnderflow")
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.is_empty() is not True
    # print(s.pop())
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
