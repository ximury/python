from datetime import datetime

day_seconds = 24 * 3600
time_test = 1601075210
str = 'strlog-2022.04.28'
res = str.split('-')[-1]
print(res)
day_start = int(datetime.strptime(res, '%Y.%m.%d').timestamp())
print(day_start)

if day_start < time_test < (day_start + day_seconds):
    print(True)
else:
    print(False)

date_user_online_time_dict = {
    # 用户名会重复，比如 kylin
    "2022.04.27": {
        "kylin|t1.qwe.local": [("终端登录", 1651075200), ("终端登出", 1651075300)],
        "kylin|t2.qwe.local": [("终端登录", 1651075200), ("终端登出", 1651075300)],
        "user1|t2.qwe.local": [("终端登出", 1651075200), ("终端锁屏", 1651076200), ("终端解锁", 1651078200)]
    },
    "2022.04.28": {
        "kylin|t1.qwe.local": [("终端登录", 1651075200), ("终端登出", 1651075300)],
        "user1|t3.qwe.local": [("终端登出", 1651075200), ]
    }
}

for user_online_time_dict in date_user_online_time_dict:
    print(user_online_time_dict)

test1 = {"user1|t3.qwe.local": [("终端登出", 1651075200), ]}
# test1 = {"user1|t3.qwe.local": []}
k = "user1|t3.qwe.local"
v = test1.get(k)
print(v)
# v = [(1, )]
for item in v:
    a1 = item[0]
    a2 = item[1]
    print(a1, a2)