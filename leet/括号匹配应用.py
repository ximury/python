from leet.栈 import SStack

dic = {
    '2022.04.23|0419-4|4SAQ-NXEG-QFKG-QMWX-LX7Z|登录': 4,
    '2022.04.23|kylin|HQSJ-6URV-FNYB-MMK5-BAAL|登录': 2,
    '2022.04.23|kylin|HQSJ-6URV-FNYB-MMK5-BAAL|登录': 3,
    '2022.04.23|kylin|BNTL-6E3Q-X9TS-TSMF-SKVT|登录': 1,
    '2022.04.23|0419-4|4SAQ-NXEG-QFKG-QMWX-LX7Z|登出': 5,
    '2022.04.23|kylin|HQSJ-6URV-FNYB-MMK5-BAAL|登出': 6,
    '2022.04.23|cas|AAAA-6URV-FNYB-MMK5-BAAL|登出': 7,
}
start = 0
end = 10
# 9 4 1 7 = 21

li = [
    '2022.04.23|0419-4|4SAQ-NXEG-QFKG-QMWX-LX7Z|登录',
    '2022.04.23|kylin|BNTL-6E3Q-X9TS-TSMF-SKVT|登录',
    '2022.04.23|kylin|HQSJ-6URV-FNYB-MMK5-BAAL|登录',
    '2022.04.23|kylin|HQSJ-6URV-FNYB-MMK5-BAAL|登录',
    '2022.04.23|0419-4|4SAQ-NXEG-QFKG-QMWX-LX7Z|登出',
    '2022.04.23|kylin|HQSJ-6URV-FNYB-MMK5-BAAL|登出',
    '2022.04.23|cas|AAAA-6URV-FNYB-MMK5-BAAL|登出'
]

li = dic.keys()
print(li)


left_parens = []
right_parens = []
keys = []
login_logout_dict = {}
for index, value in enumerate(li):
    print(index, value)
    type = value.split('|')[-1]
    key = '|'.join(value.split("|")[:-1]) + "|"
    if key not in keys:
        keys.append(key)
    # print(type)
    print(key)
    if type == '登录' and value not in left_parens:
        left_parens.append(value)
    elif type == '登出' and value not in right_parens:
        right_parens.append(value)
    print(left_parens, right_parens)
print("************")

for item in keys:
    login_logout_dict[item + "登录"] = item + "登出"
print(login_logout_dict)

total = 0

# stack = SStack()
# for index, value in enumerate(li):
#     print(stack.__dict__, value)
#     if value in left_parens:
#         stack.push(value)
#     elif value in right_parens:
#         if stack.is_empty():
#             print(False)
#         print(login_logout_dict.get(value), end="**\n")
#         print(stack.pop(), end="***\n")
#         total += dic.get(value)
        # if login_logout_dict.get(value) != stack.pop():
        #     print(False)

# print(stack.__dict__)
# print(total)

print("**********************")
stack = []

for index, value in enumerate(li):
    print(value)
    # if value in left_parens:
    #     stack.append(value)
    # elif value in right_parens:
    if value in right_parens:
        stack.append(value)
print(stack, end="---------------\n")
for index, value in enumerate(li):
    if value in left_parens:
        login_time = dic.get(value)
        logout_key = login_logout_dict.get(value)
        logout_time = dic.get(logout_key)
        print(login_time, logout_time, logout_key)
        if logout_key in stack:
            stack.remove(logout_key)
            left_parens.remove(value)
            right_parens.remove(logout_key)
            print(logout_key, end="**&\n")
            total += (logout_time - login_time)
print(total)
print(left_parens)
print(right_parens)