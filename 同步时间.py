one_hour = 3600
day_seconds = 24 * one_hour
date_user_online_time_dict = {
    '2022.04.22':  # 1650556800
        {
            'kylin|save6.qwe.local':
                [
                    ('终端解锁', 1650596839),  # 0
                    ('终端登出', 1650598630),  # +1791
                    ('终端登录', 1650598830),  #
                    ('终端锁屏', 1650598988),  # +158
                    ('终端解锁', 1650607988)   # + (1650556800 + 24*3600 - 1650607988) = + 35212
                ],
            'kylin|cai.qwe.local':
                [
                    ('终端登出', 1650615643),  # +58843
                    ('终端锁屏', 1650615743),  #
                    ('终端解锁', 1650616800),  #
                    ('终端登录', 1650617000),  # +(1650556800 + 24*3600 - 1650617000) = +26200
                ],
            'kylin|cai12.qwe.local':
                [
                    ('终端锁屏', 1650619739), ('终端锁屏', 1650620372),
                    ('终端解锁', 1650623434), ('终端锁屏', 1650623741),
                    ('终端解锁', 1650632368), ('终端锁屏', 1650633598),
                    ('终端解锁', 1650633919), ('终端锁屏', 1650634318),
                    ('终端解锁', 1650634718), ('终端锁屏', 1650635020),
                    ('终端解锁', 1650635663), ('终端锁屏', 1650636062),
                    ('终端解锁', 1650636572), ('终端锁屏', 1650619092),
                    ('终端锁屏', 1650638553), ('终端解锁', 1650641588),
                    ('终端锁屏', 1650642839)
                ]
        }
}

into_list = ["终端登录", "终端解锁"]
out_list = ["终端登出", "终端锁屏"]


def get_user_total_online_time(day_start_time, action_time_list):
    online_time = 0
    start_action = False  # in是True，out是False
    in_action_time = 0
    out_action_time = 0
    in_action_num = 0
    for action_time_set in action_time_list:
        # 终端登出后终端锁屏，按照第一个的out操作时间计算，之后紧接着有out操作不做任何计算
        if start_action is False and action_time_set[0] in out_list:
            start_action = True
            online_time = (action_time_set[1] - day_start_time)
        else:
            if action_time_set[0] in into_list:
                start_action = True
                in_action_time = action_time_set[1]
                in_action_num += 1
            # 如果有两个登录，或者终端解锁后登录，按照最后一个in操作时间计算
            elif action_time_set[0] in out_list and in_action_num > 0:
                out_action_time = action_time_set[1]
                online_time += (out_action_time - in_action_time)
                in_action_num = 0
                # elif in_action_num > 1:
                #     in_action_num -= 1
            # if action_time_set[0] in out_list and in_action_num == 1:
            if in_action_num > 1:
                print("ERROR: {}".format(action_time_set))
    print("最后时间之前的在线时长总和：" + str(online_time))
    if in_action_num != 0:
        online_time += (day_start_time + day_seconds - in_action_time)
    return online_time


if __name__ == '__main__':
    for date in date_user_online_time_dict:
        user_online_time_dict = date_user_online_time_dict.get(date)
        for user in user_online_time_dict:
            action_time_list = user_online_time_dict.get(user)
            print(action_time_list)
            print("*********************")
            online_time = get_user_total_online_time(day_start_time=1650556800, action_time_list=action_time_list)
            print(online_time)
            print(str(online_time / one_hour) + "小时")
            print("------------END-------------")