import datetime2

a = str(datetime2.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + \
    ' 星期：' + str(datetime2.datetime.now().isoweekday())

print(a)

print(datetime2.datetime.utcnow())
print(datetime2.datetime.now())

print("**************************")
text = "2020-12-25 07:12:58.261033"
text2 = "2020-12-29T08:50:46.670Z"
text3 = 'ISODate("2020-12-29T07:18:20.172Z")'
text4 = "2020-10-22 11:25:47"

# print(datetime.datetime..now())


def utc2local(utctime_str):
    utc_dtm = datetime2.datetime.strptime(utctime_str, '%Y-%m-%d %H:%M:%S.%f')
    # UTC 时间转本地时间（ +8:00 ）
    local_time = datetime2.datetime.fromtimestamp(0)
    utc_time = datetime2.datetime.utcfromtimestamp(0)
    offset = local_time - utc_time
    return utc_dtm + offset


print(utc2local(text4))
