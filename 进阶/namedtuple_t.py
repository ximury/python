from collections import namedtuple

user_info = namedtuple('user_obj', ['name', 'age', 'phone', 'email'])
user1 = user_info('admin', '18', '13578451256', '13578451256@163.com')
print(type(user1), user1)
print(user1.name)
print(user1.age)
user2 = user_info('demo', '19', '13512345678', '13512345678@163.com')
user3 = user_info('user03', '35', '13875456545', '13875456545@163.com')
user_list = [user1, user2, user3]
for i in user_list:
    print(i.name)
