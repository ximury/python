from leet.栈 import SStack, Stack


def check_parens(text):
    stack = SStack()
    left_parens = "([{"
    right_parens = ")]}"
    parens = {")": "(", "]": "[", "}": "{"}
    for i in text:
        if i in left_parens:
            stack.push(i)
        elif i in right_parens:
            if stack.is_empty():
                return False
            if parens[i] != stack.pop():
                return False
    if stack.is_empty():
        return True
    return False


def check_parens2(string):
    stack = Stack()
    check_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for char in string:
        if char in {'(', '[', '{'}:
            stack.push(char)
        elif char in {')', ']', '}'} and len(stack.stack) > 0:
            if stack.gettop() == check_dict[char]:
                stack.pop()
        else:
            return False
    if len(stack.stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check_parens("([{1232})]"))
    assert check_parens("[{1232}]") is True
    assert check_parens("[{[}]") is False
    assert check_parens("[{123444]}]") is False
    assert check_parens("][{}]") is False

    print(check_parens2('{[()]}()[{()}]'))
