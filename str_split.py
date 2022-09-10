a = '2893hccjw,d82.d29,du82'

# 想要结果： d82.d29,du82
print(a.index(','))
str = ''
if a.index(',') > 0:
    str = a.split(',')[1:]

print(str)

str = ''.join(str)

print(str)

num = a.index(',')
print(num)

str = a[num + 1:]
print(str)

print('-------------------')
a = '2 893hccjw,d82.d29,du82'
# print(a.index(' '))
# str = a[a.index(' ')+1:]
# print(str)
if ' ' in a:
    str = a[a.index(' ') + 1:]
    print(str)
    str = a[:a.index(' ')]
    print(str)

print('____________________________')
str = 'application./wps-office.xlsx'
print(str.index('.'))
res = ''
if str.index('.') > 0:
    res = str.split('.')[-1]
print(res)

str2 = 'sbxiuuwe'
print(str2.split('.')[-1])

str3 = 'NTP_SERVERS="abc"'
res = str3.split('"')
print(res)
print(res[1])

print('____________________________')

str = "/opt/script/0d70cbe73f684679bf2acdea4b1aa517.sh"
print(str.split('/')[-1])

print('____________________________')

user_info = '12ce0101d9a741d9b713686b94ea7e91|t1|84238fe82bd24b93855abb4a53be6b44'
print(user_info.split("|"))
user_info = user_info.split("|")
# print(type(res))
print(user_info[0])
first = user_info[0],
print(user_info[0])
print(first)

# terminal_user_id = user_info.split("|")[0],
# terminal_user_name = user_info.split("|")[1]
# terminal_user_area_id = user_info.split("|")[2]
# print(terminal_user_id)
# print(type(terminal_user_area_id))
# print(terminal_user_name)
# print(terminal_user_area_id)

print("************************")

video_file_dir = "/home/apt-data/static/vnc/"
res = video_file_dir.split("/")[-2]
print(res)

print("----------")
video_file_dir = "/home/apt-data/static//"
res = video_file_dir.split("/")[-2]
print(res)
