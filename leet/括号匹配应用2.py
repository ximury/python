
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


def get_left_right_list(li):
    keys = []
    left_parens = []
    right_parens = []
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
    return {"left_parens": left_parens, "right_parens": right_parens, "login_logout_dict": login_logout_dict}


if __name__ == '__main__':
    res = get_left_right_list(dic.keys())
    for key in dic:
        key1 = '|'.join(key.split("|")[:-1]) + "|"