import hashlib

old_password = 'Kim.1997'
password = ''

hl = hashlib.md5()
print(old_password, password)
hl.update(old_password.encode(encoding="utf-8"))
old_password = hl.hexdigest()
hl = hashlib.md5()
hl.update(password.encode(encoding="utf-8"))
password = hl.hexdigest()
print(old_password, password)
